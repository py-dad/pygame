#!/usr/bin/env python3
"""
Generate a Substack-ready Markdown newsletter from YAML or JSON input.

Features:
- Auto weather via NWS API (no key required), with multiple locations
- Top stories + per-story sources
- Optional extra_sources
- Appends a deduped Sources section at bottom

Usage:
  python make_newsletter.py newsletter.yaml > draft.md
  python make_newsletter.py newsletter.json > draft.md

Dependencies:
  pip install pyyaml requests
"""

from __future__ import annotations
from datetime import datetime
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

import requests


def load_input(path: Path) -> Dict[str, Any]:
    suffix = path.suffix.lower()
    raw = path.read_text(encoding="utf-8")

    if suffix in (".yaml", ".yml"):
        if yaml is None:
            raise RuntimeError("PyYAML not installed. Run: pip install pyyaml")
        return yaml.safe_load(raw) or {}
    elif suffix == ".json":
        return json.loads(raw)
    else:
        raise ValueError("Input file must be .yaml/.yml or .json")


def _require(data: Dict[str, Any], key: str) -> Any:
    if key not in data or data[key] in (None, ""):
        raise KeyError(f"Missing required field: {key}")
    return data[key]


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _safe_str(x: Any) -> str:
    return str(x).strip()


@dataclass
class WeatherLine:
    line: str
    source_url: str


def fetch_nws_weather_one_liner(lat: float, lon: float, label: Optional[str] = None) -> WeatherLine:
    """
    Uses NWS API:
      1) GET https://api.weather.gov/points/{lat},{lon}
      2) From that, use "forecast" URL to get forecast periods
    Returns a single line suitable for the newsletter.
    """
    headers = {
        # NWS requests a real User-Agent with contact info.
        # Replace email later if you want.
        "User-Agent": "MaconCountyMorningUpdate/1.0 (contact: keith@example.com)",
        "Accept": "application/geo+json",
    }

    points_url = f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}"
    r = requests.get(points_url, headers=headers, timeout=15)
    r.raise_for_status()
    points = r.json()

    forecast_url = points["properties"]["forecast"]

    rf = requests.get(forecast_url, headers=headers, timeout=15)
    rf.raise_for_status()
    forecast = rf.json()

    periods = forecast["properties"]["periods"]
    if not periods:
        raise RuntimeError("NWS returned no forecast periods.")

    # First period is usually Today/This Afternoon depending on time.
    p0 = periods[0]
    name = _safe_str(p0.get("name", "Today"))
    short = _safe_str(p0.get("shortForecast", "")).rstrip(".")
    temp = p0.get("temperature")
    temp_unit = _safe_str(p0.get("temperatureUnit", "F"))

    # Try to find Tonight for a low (optional).
    low_part = ""
    tonight = None
    for p in periods[1:5]:
        if "tonight" in _safe_str(p.get("name", "")).lower():
            tonight = p
            break
    if tonight and tonight.get("temperature") is not None:
        low_part = f", low {tonight['temperature']}{_safe_str(tonight.get('temperatureUnit','F'))}"

    where = f"{label}: " if label else ""
    line = f"Weather ({where}{name}): {short}. {temp}{temp_unit}{low_part}."

    return WeatherLine(line=line, source_url=forecast_url)


def fetch_multiple_weather_lines(locations: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
    lines: List[str] = []
    source_urls: List[str] = []

    for loc in locations:
        wl = fetch_nws_weather_one_liner(
            lat=float(loc["lat"]),
            lon=float(loc["lon"]),
            label=_safe_str(loc.get("label", "")) or None
        )
        lines.append(wl.line)
        source_urls.append(wl.source_url)

    return lines, source_urls


def format_newsletter(data: Dict[str, Any]) -> str:
    title = _require(data, "title")
    now = datetime.now()
    date = data.get("date")
    if not date:
        date = now.strftime("%A, %B ") + str(now.day)

    intro = _require(data, "intro")
    byline = _safe_str(data.get("byline", ""))

    top_stories: List[Dict[str, Any]] = data.get("top_stories", [])
    quick_hits: List[str] = [_safe_str(x) for x in data.get("quick_hits", []) if _safe_str(x)]
    coming_up: List[str] = [_safe_str(x) for x in data.get("coming_up", []) if _safe_str(x)]

    # Weather: auto if enabled, else manual
    weather_auto = data.get("weather_auto", {}) or {}
    weather_lines: List[str] = []
    weather_source_urls: List[str] = []

    if bool(weather_auto.get("enabled", False)):
        locations = weather_auto.get("locations", [])
        if not locations:
            raise KeyError("weather_auto.enabled is true but no locations were provided")
        weather_lines, weather_source_urls = fetch_multiple_weather_lines(locations)
    else:
        weather_lines = [_safe_str(_require(data, "weather"))]

    # Collect sources for bottom section
    sources_out: List[Tuple[str, str]] = []  # (label, url)

    def add_source(label: str, url: str):
        label = label.strip()
        url = url.strip()
        if not url:
            return
        sources_out.append((label or url, url))

    # Weather sources (dedupe later)
    for url in weather_source_urls:
        add_source("NWS forecast", url)

    lines: List[str] = []
    lines.append(_safe_str(title))
    lines.append(_safe_str(date))
    lines.append("")
    lines.append(_safe_str(intro))
    lines.append("")
    lines.append("Weather:")
    for wl in weather_lines:
        lines.append(wl)
    lines.append("")

    # Top stories: up to 3
    for idx, story in enumerate(top_stories[:3], start=1):
        headline = _safe_str(story.get("headline", ""))
        if not headline:
            continue

        lines.append(f"{idx}) {headline}")

        body = story.get("body", [])
        if isinstance(body, str):
            body = [body]

        # Output up to 3 sentences to keep it tight
        for sentence in _as_list(body)[:3]:
            s = _safe_str(sentence)
            if s:
                lines.append(s)

        # Story sources
        story_sources = _as_list(story.get("sources", []))
        clean_urls = [_safe_str(u) for u in story_sources if _safe_str(u)]
        if clean_urls:
            if len(clean_urls) == 1:
                lines.append(f"Source: {clean_urls[0]}")
                add_source(headline, clean_urls[0])
            else:
                lines.append("Sources:")
                for u in clean_urls:
                    lines.append(f"- {u}")
                    add_source(headline, u)

        lines.append("")

    # Quick hits
    if quick_hits:
        lines.append("Also worth noting:")
        for item in quick_hits:
            lines.append(f"– {item}")
        lines.append("")

    # Coming up
    if coming_up:
        lines.append("What’s coming up:")
        for item in coming_up:
            lines.append(f"– {item}")
        lines.append("")

    # Optional extra sources
    extra_sources = data.get("extra_sources", []) or []
    for entry in extra_sources:
        if isinstance(entry, dict):
            add_source(_safe_str(entry.get("label", "")), _safe_str(entry.get("url", "")))

    # Bottom Sources section (deduped)
    if sources_out:
        seen = set()
        deduped: List[Tuple[str, str]] = []
        for label, url in sources_out:
            if url in seen:
                continue
            seen.add(url)
            deduped.append((label, url))

        lines.append("Sources:")
        for label, url in deduped:
            lines.append(f"- {label}: {url}")
        lines.append("")

    if byline:
        lines.append("—")
        lines.append(f"By {byline}")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python make_newsletter.py <newsletter.yaml|newsletter.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    try:
        data = load_input(path)
        output = format_newsletter(data)
    except requests.RequestException as e:
        print(f"Weather fetch error: {e}", file=sys.stderr)
        print("Tip: set weather_auto.enabled: false and provide 'weather:' manually.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

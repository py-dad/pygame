import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def main():
    csv_path = "c:\\pythonprojects\\trint-mood.csv"

    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("File not found. Please check your path and try again.")
        return
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        return

    if not {'Date', 'Score'}.issubset(df.columns):
        print("CSV must contain 'Date' and 'Score' columns.")
        return

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values('Date')

    # Optional: strip time part if your data includes timestamps
    df['Date'] = df['Date'].dt.date

    plt.figure(figsize=(8, 5))
    plt.plot(df['Date'], df['Score'], marker='o', linestyle='-', color='blue')
    plt.title('Score Over Time')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.grid(True)

    # Format x-axis to show only dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

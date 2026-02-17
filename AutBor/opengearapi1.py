import requests
from requests.auth import HTTPBasicAuth

base_url = "https://192.168.0.1/api/v2"
username = "root"
password = "KC'TfG=Fi.TtF%Qs"

requests.packages.urllib3.disable_warnings()

response = requests.get(
    base_url + "system",
    auth=HTTPBasicAuth(username, password),
    verify=False # ignore ssl cert check
)

if response.status_code == 200:
    data = response.json()
    print("System Info:")
    print(data)
else:
    print("Error", response.status_code, response.text)
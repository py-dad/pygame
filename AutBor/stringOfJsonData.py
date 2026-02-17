import json
stringofJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonD = json.loads(stringofJsonData)

print(type(stringofJsonData))

print(type(jsonD))

print(jsonD)
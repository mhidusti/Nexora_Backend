import requests

url = "https://pro-api.coinmarketcap.com/public-api/v1/simple/price"

params = {
    "ids": "1,1027",
    "convert": "USD",
}

response = requests.get(url, params=params, timeout=10)

print(response.status_code)
print(response.text)
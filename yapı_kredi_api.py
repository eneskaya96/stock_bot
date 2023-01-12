


import requests

x = requests.get("https://api.yapikredi.com.tr/api/stockmarket/v1/bistIndices")

print(x.text)
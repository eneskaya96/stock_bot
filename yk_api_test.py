import requests



url = " https://api.yapikredi.com.tr/auth/oauth/v2/token"
x = requests.post(url)

print(x.text)
print("---------")


url = 'https://api.yapikredi.com.tr/api/stockmarket/v1/bistIndices'

headers = {  'Authorization':'Basic ZW5lc2theWExOTk2OjI1NjE0M0VrLiE='  }

x = requests.post(url, headers=headers)
print(x.text)





print(x.status_code)
import httpx
import requests

s= requests.Session()#自动处理cookie

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'Content-Type': 'application/json',
}
url='https://stageapi.testhtm.com/v1/users/login'
data = '{"email":"daiataowei@hiretual.com","password":"Hkj20210705@"}'
s.get(url)
response = httpx.post(url, headers=headers, data= data)
h=response.headers
csrf =h['set-cookie'][10:25]
print(f'headers:{h},csrf:{csrf},session:{s}')

# print('resp', response.cookies._cookies)
# print('req',  response.request._cookies._cookies)






# 1.记得安装 第三方 模块 requests
# pip install requests


import requests


class RequestSpider(object):
    def __init__(self):
        url = 'https://stageapi.testhtm.com/v1/users/login'

        headers = {
            'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
            'Content-Type': 'application/json',
        }

        data = '{"email":"daiataowei@hiretual.com","password":"Hkj20210705@"}'

        #response = httpx.post('https://stageapi.testhtm.com/v1/users/login', headers=headers, data=data)
        self.response = requests.post(url, headers=headers,data=data)

    def run(self):
        data = self.response.content

        # 1.获取请求头
        request_headers = self.response.request.headers

        # 2.获取相应头
        coderesponse_headers = self.response.headers

        # 3.响应状态码
        code = self.response.status_code

        # 4. 请求的cookie 注意写法
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 5. 响应的cookie
        response_cookie = self.response.cookies

        print(response_cookie)


RequestSpider().run()

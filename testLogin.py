import requests
companylist=["greenhouse-harvest","breezy","beameryfrontier","bullhorn","clinch","crelate","jobadder","zoho","workday","lever","workable","cats","jazzhr","pcrecruiter",
             "jobvite"]
for i in companylist:
    url = "https://api.testhtm.com/v1/integrations/updateFusionStatus?company={i}&fusionStatus=1"

    payload={}
    headers = {
   'Cookie': '_ga=GA1.2.996415829.1626935825; _hjid=b4bbec22-8e85-4ac7-8939-af17811cad6e; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1626935925965-0%22%2C%22c%22%3A1626935925974%2C%22l%22%3A1626935925974%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22c545d6a4-5fda-8aed-1bfb-b702bce2a7f1%22%2C%22c%22%3A1626935925977%2C%22l%22%3A1626935925977%7D; _hjSessionUser_1537703=eyJpZCI6IjkyYjI3MGE2LTczYzUtNTk2NS04NWMwLTgwMDg5YmU4YTExZSIsImNyZWF0ZWQiOjE2MzcyOTg2OTcxNjIsImV4aXN0aW5nIjp0cnVlfQ==; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%224e2907f4-ca5e-368a-0265-190c389405e1%22%2C%22e%22%3A2151218947441%2C%22c%22%3A1631256601890%2C%22l%22%3A1651218947441%7D; _gid=GA1.2.1784178221.1652773949; csrfToken=aRtyMmRPb1fCWwe; hiretual_session=s%3Asession%3A28092510-d756-11ec-8607-d3e6d1af2c21.ejM9V8WJG6xpfgEom0uUILP0nIRCrY4vksg3Sac7JCQ; intercom-session-vn70vifr=dzVPM01SSlNUbDRuWUs2c1JRV2p4SnFTVS9sRGttdUdWS3lCSkovWURpYlliYXZWelFhQmV0SjBVOUJ4WURlOC0tajZQZ1V2UC83c1NsVzlRTFpCODVGZz09--26615d94c5787f04d5e94e5ce0c495bb3b834234',
   'csrf-token': 'aRtyMmRPb1fCWwe',
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
import os
from urllib import request,parse
import socket
import http .cookiejar, urllib.request
import opener as opener
import requests
from urllib.parse import urlparse
import re
# url='http://192.168.8.26:88/api/SalesCustomer/ImportCustomers'
# herder={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# }
# coo={
#     "Cookie":"zentaosid=je3nt4ivtqjfvsv2tlchd3bfg0; .AspNet.Cookies=0yr8REmwHXKAJi18nYI8dMSdrChXD8aFsPDz4nXq2fWXO2Czv5UWSnIO3Dh99QCJxknntKsjBgkhQbmxO9nol_PZ0dOtpU9h12vkKRvEg2b-sj8XQHEnMOkt54rY7BjP6wbCPSKWxFl_ifLHMHNa1Szhw--ENlrgD5Y1KKZwFBnyczSm9sgXtSSylwfOl9yIqT4P_sLUwTcJOShkSJymXdm_TCLjA4hcSmDbiLrOmQS1mVzfIaGpMkvos6CYJm1ZI1PkF3NoZq7zbLPh7iBWgEGgpQM97pkZwuOCFkkWkti1s__JHTPzfMU11cuIm5ScTl_k_miXDocJ35VSgF03XyBx49SnlkADU9Q3s-HZ5gz5DV4GTwd9opwrwl2PBqblbz6nKmZ4IEV3LAhfDbC3VkM25bpmh7QFXo0ktSFNh5n88dDeXvm0Yo4RrMYMIUs7y-Ar0EF6Dw4EuDoVmc-ly55axYAPV1FAENA79321VSazSBt6_XMNZGjxKunqIQaGN2XRLvaAYjpAD2xzdBVIglb385c88bvXqsvCZwlN3OFXU0He8rXJL8ORWDyzK2-A7W_NTL317By5HVSKqh3Bo0GNOlYOR5LfJveLSfX_QFRjMgFTTjldHisCD8Xork4VwX1y9-I66ANuoSx_EU7SHrqzeMbKTQ_X4_GFavX9KDTZsAz4Uoy8iClNbcaB-g7IcrOipISbwTuvnOLnOqHAsDC-3u06BQJw7dhh1UXMzUCwXQn-YbhRZPpEKFv6SxqJqJEC9cr4iwYDil5d-7Gw9M8g_w7sxE1DvLfRclHnUfrZlfsW3eLXOwO-ckhCGFbr; token=oV6h_OA5b6jZ5-1DQsRNLXsQENBe36MV8bg7dYhZb4P_nIRbt9td401nLGROsQcjxDVWD4F7Bt2bYfWDmDm2al8fJT8F6QR3_UIGaFLA9DodsTcIeOzNjqQdH4qpStomGaJQDT1tNSbpN9e-uJgHfE9UEeQfv4ky2M9NN_KridoY1plkNpUqgrWYjaX0qygGeRhVZHSVvO5CRbL5uYYrXoT0oa4mdmxcnHx1672w8CefNxz6wRUXnsfPfb512iinvyF3yk1ed_9ZbCKLBqgMi8XAGWuOmtqzq7RtsBKD8A-y7zXmtas9shsoVTIMPusPb1Tx_Cw4MNg1-pO9_EausGWjiCrfuwNlvbKC0ykAJDZnsbe85a4u6_fWYIVEp6eVRQRxgpMUVhOdraP9c0fUB3QFSwacT-pfTrfbnLYFu6OAT2b2YKlB9vmnmyJ9d6vzG9jasxUkk20P_i1jrwEXqyPvGleGh1uEAuQPpaddjVWX8DMje_RT9QAiS9c1e8QbE8XoFvxXClR297eW0_Y2JOI_9arrNcccdfiCiCezdDk99K4ZUdYSPPNd6N5luTaG6XW2lGgUdQJb46NuNiGodQSoDFfxbpZVLGAar2Y55-FiqLv4T8b3GOm9dHnbw8O0IAurKm6tqZYfeTAda5gLmQg9IN-ym4BseL_GBi8GegoI1gkag1I4WWBwqEjik1t7asuVy-VIWry0_NIzB11URvIppXkjUIhubo6J0fLLze2LUh_Qkqtdi71H0GzjzYhjmFwizVs8HuaE1Hp8kgHtGDMdxuNvaN3wx8XTNWA_BakVmC3fz34kWwJrEXk2zVE9"
# }
# dict={
#     "o":"NMSL"
# }
def dowloard(html):
    pars=re.findall('<img.*?src="([a-zA-z].*?)"',html,re.S)
    i=1
    for key in pars:
        # print("开始下载"+str(i)+key+"\r\n")
        # pic=requests.get(key,timeout=10)
        # name=str(i)+'.jpg'
        # fp=open(name,'wb')
        # fp.write(pic.content)
        # fp.close()
        i+=1


def main(url,header):
    r=requests.get(url,headers=header)
    html=r.text
    dowloard(html)
if __name__ == '__main__':
    url='https://movie.douban.com/chart'
    herder = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    main(url,herder)













# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)


#文件上传
# file={'file':open('批量导出社保规则修改历史模板.xlsx','rb')}
# r=requests.post(url,files=file,cookies=coo)
# print(r.text)


# result=urlparse('www.baiducom/index.htrser?id=S#comment',scheme='https')
# print(result)

# da=bytes(parse.urlencode(dict),encoding='utf-8')
# parse.urlencode #转换成str  bytest转换成字节流
# re=request.Request(url=url,headers=herder,data=da,method='POST')
# response=request.urlopen(re)
# print(response.read().decode('utf-8'))

# r=requests.get('https://www.zhihu.com/explor',headers=herder)
# print(r.text)

# r=requests.get('http://httpbin.org/get',params=dict)
# print(r.text)


#获取cookie
# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# openerr=urllib.request.build_opener(handler)
# response=openerr.open('https://www.zhihu.com')
# for item in cookie:
#     print(item.name+'='+item.value)





#异常处理超时
# try:
#     respons = urllib.request.urlopen(url, data=da, timeout=0.1)
#     print(respons.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e.reason)









# print(re.status)#状态码
# print(re.getheaders())#响应头
# print(re.getheader('content-type'))

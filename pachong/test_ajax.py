from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url='https://m.weibo.cn/api/container/getIndex?'
header={
    "Referer":"https://m.weibo.cn/u/2830678474",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
def reques(page):
    params={
        'type':'uid',
        'value':'5631791628',
        'containerid':'1076035631791628',
        'page':page
    }
    url=base_url+urlencode(params)
    try:
        r=requests.get(url,headers=header)
        if r.status_code==200:
            return r.json()
    except requests.ConnectionError as e:
        print('Error',e.args)
def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            # weibo['id']=item.get('id')
            # weibo['text']=pq(item.get('text')).text()
            weibo['original_pic']=item.get('original_pic')
            yield weibo
            # return weibo
def dowload(url):
    for i in url:
        print(url)
        # if url[i] !=None:
        #     r=requests.get(url[i],stream=True)
        #     print('开始下载'+'.jpg')
        #     q=r.content
        #     f = open("这是一张悲伤的图片" + '.jpg', 'wb')
        #     f.write(q)
        #     f.close()


if __name__ == '__main__':
    for i in range(1,11):
        rr=reques(i)
        results=parse_page(rr)
        for result in results:
            # print(result)
            dowload(result)

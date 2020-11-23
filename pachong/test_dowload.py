import os
import re
import requests
class test_dowloard():
    def __init__(self,url,header):
        self.url=url
        self.header=header
    def dowloa(self,p):
        i=1
        path='D:\py\\relax_pachong\dowload'
        if not os.path.exists(path):
            os.makedirs(path)
            print('创建成功')
        else:
            print('创建失败')
        for address in p:
            os.chdir(path)
            print("开始下载:"+address+'\r\n')
            pic=requests.get(address,timeout=10)
            name="图片"+str(i)+'.jpg'
            f=open(name,'wb')
            f.write(pic.content)
            f.close()
            i+=1
    def parse(self,html):
        parse=re.findall('<img.*?src="([a-zA-Z].*?)"',html)
        return parse
    def main(self):
        r=requests.get(self.url,headers=self.header)
        rr=r.text
        return rr
if __name__ == '__main__':
    url='https://movie.douban.com/chart'
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    m=test_dowloard(url,header)
    q=m.main()
    print(q)
    par=m.parse(q)
    m.dowloa(par)
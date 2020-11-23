import json
import re

import requests
url='http://pvp.qq.com/web201605/js/herolist.json'
herder={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
r=requests.get(url,headers=herder)
rr=r.text
print(rr)
jsonfile=json.loads(url)
# print(jsonfile)
# parser=re.findall('sInfoImageA[a-zA-Z].*?:"(.*?)"',rr)
# print(parser)

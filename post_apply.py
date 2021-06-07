import requests
import re
import json
import os
import urllib
import argparse
parser = argparse.ArgumentParser(description='paper search')
parser.add_argument('-url',type=str)
args = parser.parse_args()

def getpage(url):
    
    querystring = {}
    method = "GET"

    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'cache-control': "no-cache",
        'postman-token': "524d22a5-6f66-096b-08df-ccef375e8ebc",
        }
    cookies={
        'PHPSESSID':PHPSESSID,\
        'wyQiantai_name':wyQiantai_name,
        'wyQiantai_num':wyQiantai_num
    }
    response = requests.request(method, url, headers=headers, params=querystring, cookies=cookies)
    rtxt = response.text
    return rtxt

# 全局信息
wyQiantai_name = urllib.parse.quote("这里要填你的姓名")
wyQiantai_num = "这里要填你的学号"
PHPSESSID = "这里要填你的cookie"

pageurl = args.url
content = getpage(pageurl)
# print(content)

conid = re.findall(r"var conid=\"(.+?)\";",content)[0]
sing = re.findall(r"var sing=\"(.+?)\";",content)[0]
vid = re.findall(r"vid:(.+?),tid:",content)[0]
tid = re.findall(r"tid:(.+?)},function",content)[0]

print(conid, sing, vid, tid)

def post_apply(videokey, videonum, ct):


    url = f"http://dxonline.ruc.edu.cn/index.php?s=/Videoclock/index.html&videokey={videokey}&videonum={videonum}&ct={ct}"
    querystring = {}
    method = "GET"

    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'cache-control': "no-cache",
        'postman-token': "524d22a5-6f66-096b-08df-ccef375e8ebc",
        }
    # =; PHPSESSID=esrr3scjj3rvjucsn8t4dekaot
    cookies={
        'PHPSESSID':PHPSESSID,\
        'wyQiantai_name':wyQiantai_name,
        'wyQiantai_num':wyQiantai_num
    }

    response = requests.request(method, url, headers=headers, params=querystring, cookies=cookies)
    rtxt = response.text


    return rtxt




av_sh = f'curl --location --request POST \'http://dxonline.ruc.edu.cn/index.php?s=/Index/add_videonum.html\' \
--header \'Accept: */*\think \' \
--header \'X-Requested-With: XMLHttpRequest\' \
--header \'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36\' \
--header \'Content-Type: application/x-www-form-urlencoded; charset=UTF-8\' \
--header \'Cookie: PHPSESSID={PHPSESSID}; wyQiantai_name={wyQiantai_name}; wyQiantai_num={wyQiantai_num}\' \
--data-urlencode \'tid={tid}\' \
--data-urlencode \'vid={vid}\''
os.system(av_sh)
d = post_apply(vid, 1, 0)
print(d)
d = json.loads(d)
ct = d['data']['create_time']
print(post_apply(vid, 2, ct))
print(post_apply(vid, 3, ct))
print(post_apply(vid, 4, ct))

p_sh = f"curl --location --request POST 'http://dxonline.ruc.edu.cn/index.php?s=/Index/gethours.html' \
    --header 'Accept: */*' --header 'X-Requested-With: XMLHttpRequest' --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' --header 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
            --header 'Cookie: PHPSESSID={PHPSESSID}; wyQiantai_name={wyQiantai_name}; wyQiantai_num={wyQiantai_num}' \
                --data-urlencode \'conid={conid}==' --data-urlencode 'ct={ct}' --data-urlencode 'hours=2.5' \
                    --data-urlencode 'name={wyQiantai_name}' --data-urlencode 'num={wyQiantai_num}' --data-urlencode 'sing={sing}'"
os.system(p_sh)

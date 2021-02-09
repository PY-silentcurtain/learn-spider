import requests
from lxml import etree

url = "https://music.163.com/artist?id=5771"
furl = "http://music.163.com/song/media/outer/url?id="

response = requests.get(url=url)

print(response)

html = etree.HTML(response.text)

url_list = html.xpath('//a[contains(@href,"/song?")]/@href')[:50]
name_list = html.xpath('//a[contains(@href,"/song?")]/text()')[:50]
print(url_list)
print(name_list)

for i in url_list:
    xyy = furl + i.replace('/song?id=','')
    print(xyy)

    for h in name_list:
        xyz = requests.get(url=xyy)
        with open('./topmusic/%s.mp3' % h, 'wb') as file:
            file.write(xyz.content)
        print("<%s>下载成功" % h)
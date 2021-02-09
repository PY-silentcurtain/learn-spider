import scrapy
import json
import time

class GzhSpider(scrapy.Spider):
    name = 'gzh'
    start_urls = ['https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=&type=9&query=&token=824638704&lang=zh_CN&f=json&ajax=1']

    def parse(self, response):

        gzh_json = json.loads(
            str(response.body, encoding='utf-8'),
            encoding='utf-8'
        )

        txt1 = gzh_json['app_msg_list']

        for data in txt1:
            title = data['title']
            url = data['link']
            print(title)
            print('url->' + url)

        time.sleep(3)

        yield {
            "title": title,
            "url": url
        }

        i = 0
        for h in range(14):
            i = i + 5
            x = str(i)
            next = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=" + x  + "&count=5&fakeid=&type=9&query=&token=824638704&lang=zh_CN&f=json&ajax=1"
            yield scrapy.Request(next)
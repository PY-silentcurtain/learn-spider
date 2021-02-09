import scrapy
import json

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['alicdn.com']
    start_urls = ['https://tce.alicdn.com/api/data.htm?ids=222882%2C222883%2C222921']

    def parse(self, response):
        tb_json = json.loads(
            str(response.body,encoding='utf-8'),
            encoding='utf-8'
        )

        txt1 = tb_json['222882']
        txt2 = txt1['value']

        for data in txt2['head']:
            print(data['name'])
            print('url=>',data['link'])

        for data2 in txt2['list']:
            print(data2['name'])
            print('url=>', data2['link'])
#这部分是一开始失败的代码，我这里没有选择删除而是注释掉。
#大家结合文章内容思考一下为什么这样写代码会报错，
#爬不到我们需要的信息?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''for data in tb_json['222882']:
            for data2 in data['value']:
                for data3 in data2['head']:
                    url=data2['link']
                    title=data2['name']
                    print(title)
                    print('=>',url)'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pass
        
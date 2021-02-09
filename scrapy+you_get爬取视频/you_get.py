import scrapy
import sys
import you_get

def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()

path = r'C:\Users\86157\Desktop\MV'

class DbSpider(scrapy.Spider):
    name = 'db'
    start_urls = ['https://y.qq.com/n/yqq/playlist/3809400714.html#stat=y_new.profile.create_playlist.click&dirid=1']

    def parse(self, response):
        for ul in response.xpath('//div[@class="mod_songlist"]/ul[2]'):
            urls = ul.xpath('//a[@title="MV"]/@href').extract()
            for i in urls:
                xyy = 'https:' + i
                print(xyy)
                download(xyy, path)

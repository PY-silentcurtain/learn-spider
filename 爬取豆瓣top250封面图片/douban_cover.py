import scrapy
from ImageSpider.items import ImagespiderItem
from scrapy.pipelines.images import ImagesPipeline

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
 
    allowed_domains = ['movie.douban.com']

    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = ImagespiderItem()  # 实例化item
        #imgurls = response.xpath('//div[@class="post-content"]/p/img/@src').extract() # 注意这里是一个集合也就是多张图片
        imgurls = response.xpath('//ol[@class="grid_view"]/li//a//img/@src').extract()  # 注意这里是一个集合也就是多张图片
        item['imgurl'] = imgurls
        print(imgurls)

        next =  response.xpath('//span[@class="next"]/a/@href').extract_first()

        if next !=None:

            next_url = "https://movie.douban.com/top250" + next
            yield scrapy.Request(next_url)

        yield item
        pass
        #scrapy crawl ImgSpider

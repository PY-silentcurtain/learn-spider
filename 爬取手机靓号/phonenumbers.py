import scrapy

#http://www.jihaoba.com/escrow/
class PhoneSpider(scrapy.Spider):
    name='phone'

    start_urls=[
        'http://www.jihaoba.com/escrow/'
        ]

def parse(self, response):
for ul in response.xpath('//div[@class="numbershow"]/ul'):
            phone=ul.xpath('li[contains(@class,"number")]/a/@href').re("\\d{11}")[0]
            price=ul.xpath('li[@class="price"]/span/text()').extract_first()[1:]
            #这里我们统一一下爬取来的价格的格式。
if price.endswith('万'):
                price=int(float(price[:-1])*10000)
else:
                price=int(price)

yield {
"phone": phone,
"price": price
            }

next="http://www.jihaoba.com"+response.xpath('//a[@class="m-pages-next"]/@href').extract_first()
yield scrapy.Request(next)

'''
“//”代表跳级匹配，“/”代表是直接的父子级关系。我们可以用“@”来匹配标签中元素的内容，
如class、src、href等等需要的内容。更具体的内容请观看我们的视频讲解。
“contains”代表匹配标签里只要有你指定的元素就会被匹配出来。
若不用这个参数则元素和参数之间必须用“=”连接。一个是包含关系，一个是等于关系。
'''
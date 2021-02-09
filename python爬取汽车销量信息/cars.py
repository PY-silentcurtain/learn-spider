import scrapy
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

class CarSpider(scrapy.Spider):
    name = 'car'
    start_urls = ['http://www.515fa.com/xldp/dp_22926.html']

    def parse(self, response):
        #print(response.body)
        for div in response.xpath('//div[@class="wen1"]/div[@class="w_con"]'):
            name = div.xpath('//div[@class="w_con"]/div/strong/text()').extract()[:10]
            total = div.xpath('//div[@class="w_con"]/div/text()').re("\\d{5,6}")

        print(name)
        print(total)

        data = [go.Bar(
            x=total,
            y=name,
            orientation='h'
        )]
        layout = go.Layout(
            title='2020年1~6月汽车销量排行榜'
        )
        figure = go.Figure(data=data, layout=layout)
        pyplt(figure, filename='1.html')
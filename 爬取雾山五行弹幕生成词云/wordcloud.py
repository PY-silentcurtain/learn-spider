import scrapy
import wordcloud

class BtopSpider(scrapy.Spider):
    name = 'btop'
    start_urls = ['http://comment.bilibili.com/218796492.xml']

    def parse(self, response):
        print(response.body)

        dm = response.xpath('//d/text()').extract()
        print(dm)
        print(len(dm))

        with open('a.txt', 'w',encoding='utf-8') as f:
            for i in dm:
                f.write(i+'\n')
        f.close()

        # 从外部.txt文件中读取大段文本，存入变量txt中
        f = open('a.txt', encoding='utf-8')
        txt = f.read()

        # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
        w = wordcloud.WordCloud(width=1000,
                                height=700,
                                background_color='white',
                                font_path=r'C:\Users\86157\msyh.ttc')
        # 将txt变量传入w的generate()方法，给词云输入文字
        w.generate(txt)
        # 将词云图片导出到当前文件夹
        w.to_file('b.png') 
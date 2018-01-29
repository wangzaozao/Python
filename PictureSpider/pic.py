#-*-coding:utf8-*-
from lxml import etree
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def spider(url):
    html = requests.get(url,headers=header)

    print html.text
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="classify-main clearfix"]//div[@class="clickRecord"]//div[@class="flow-item qt-card"]/div[@class="card-img"]/a[@class="thumb-box"]/img/@src')#后面加上空格第一个就不匹配了
    print content_field
    # for each in content_field:
    #     print each


if __name__ == '__main__':
   #  pool = ThreadPool(4)
    f = open('content.txt','a')
    page = []

    newpage = 'http://www.58pic.com/tupian/beijing.html'
    spider(newpage)
       # page.append(newpage)

    # results = pool.map(spider, page)
    # pool.close()
    # pool.join()
    f.close()
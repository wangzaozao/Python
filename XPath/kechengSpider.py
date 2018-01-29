#-*-coding:utf8-*-
from lxml import etree
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 把课程信息保存到info.txt中
def saveinfo(classinfo):
    f = open('info.txt', 'a')
    f.writelines('title:' + classinfo['title']+ '\n')
    f.writelines('content:' + classinfo['content']  + '\n')
    f.writelines('classtime:' + classinfo['classtime']+ '\n')
    f.writelines('classlevel:' + classinfo['classlevel'] + '\n')
    f.writelines('learnnum:' + classinfo['learnnum'] + '\n\n')
    f.close()


# 爬虫主体
def spider(url):
    html = requests.get(url)
    #print html.text
    selector = etree.HTML(html.text.encode(html.encoding))#这里解码出问题来着
    content_field = selector.xpath('//div[@class="lesson-list"]/ul/li')
    # print content_field
    info = []
    for each in content_field:
        classinfo = {}
        classinfo['title'] = each.xpath('div[@class="lesson-infor"]/h2[@class="lesson-info-h2"]/a/text()')[0]
        classinfo['content'] = (each.xpath('div[@class="lesson-infor"]/p/text()')[0]).strip()
        classTime = (each.xpath('div[@class="lesson-infor"]/div/div/dl/dd[@class="mar-b8"]/em/text()')[0]).split()
        classinfo['classtime'] = ''.join(classTime)
        classinfo['classlevel'] = each.xpath('div[@class="lesson-infor"]/div/div/dl/dd[@class="zhongji"]/em/text()')[0]
        classinfo['learnnum'] = each.xpath('div[@class="lesson-infor"]/div[@class="timeandicon"]/div/em/text()')[0]
        info.append(classinfo)
    return info


if __name__ == '__main__':
    print u'开始爬取内容。。。'
    page = []
    # 循环用来生产不同页数的链接
    for i in range(1, 11):
        newpage = 'http://www.jikexueyuan.com/course/?pageNum=' + str(i)
        print u"第%d页" % i
        print u'正在处理页面：' + newpage
        page.append(newpage)
    for each in page:
        info = spider(each)
        for each in info:
            saveinfo(each)
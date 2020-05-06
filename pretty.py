import requests
from lxml import etree

name = 1000

headers = {"Referer":"http://",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def index_pages(number):
    url = 'https://www.mzitu.com/187081/%s' % number
    index_response = requests.get(url=url, headers=headers)
    tree = etree.HTML(index_response.text)
    img_urls = tree.xpath("//p/a/img/@src")
    return img_urls


def get_img(url):
    """下载图片并保存到指定文件夹下"""
    global name
    name += 1
    img_name = 'picture\\{}.jpg'.format(name)
    img = requests.get(url, headers=headers).content
    with open(img_name, 'wb') as save_img:
        save_img.write(img)


if __name__ == '__main__':

    for n in range(1, 50):
        print("正在爬取第{}页".format(n))
        img_url_list=index_pages(n)
        for img in img_url_list:
            get_img(img)
            print(img)



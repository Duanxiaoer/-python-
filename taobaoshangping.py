import re
import requests
from bs4 import BeautifulSoup

def getHtmlText(url, code="utf-8"):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print("爬取失败")
        return ""

def getGoodsList(html, list):
    soup = BeautifulSoup(html, "html.parser")
    reg = re.compile(r"[0-9]*.[0-9]*")
    price = soup.find_all('em', {"title": reg})
    name = soup.find_all('p', {"class": "productTitle"})
    print("抓取信息数："+str(len(price)))
    for i in range(len(price)):
        pr = price[i].text
        na = name[i].text
        list.append([pr, na])

    return list


def main():
    url = "https://list.tmall.com/search_product.htm?q=%C0%B1%CC%F5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
    list = []
    html = getHtmlText(url,"GB2312")
    list = getGoodsList(html,list)
    tplt = "{0:^10}\t{1:{2}^30}"
    print(tplt.format("价钱", "名字", chr(12288)))
    for l in list:
        print(tplt.format(l[0],l[1].strip(),chr(12288)))


main()
import requests

def getHtml(url):
    try:
        kv = {"wd": "Python"}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        return r.text
    except:
        print("爬取失败")
if __name__ == "__mian__":
    url = "http://www.baidu.com/s"
    print(getHtml(url))

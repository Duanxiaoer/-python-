import requests
import time
def getHtml(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        # print(r.text)
    except:
        print("爬取失败")

if __name__ == "__main__":
    url = "https://www.bishijie.com/kuaixun"
    timeTotal = time.perf_counter()
    for i in range(100):
        timeBegin = time.perf_counter()
        getHtml(url)
        timeEnd = time.perf_counter()
        print("第{}次爬取用时{}秒".format(i+1,(timeEnd - timeBegin)))
    timeEndTotal = time.perf_counter()
    print("共耗时{}秒".format(timeEndTotal - timeTotal))
    print("平均每次耗时{}秒".format((timeEndTotal - timeTotal)/100))


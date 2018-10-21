import requests
import os

url = "http://img0.dili360.com/pic/2018/09/26/5bab38df6fda05b20233461_t.jpg@!rw9"
path_dir = "/Users/duanqifeng/PycharmProjects/reptile"

try:
    path = path_dir + "/" + url.split("/")[-1] + ".jpg"
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")

except:
    print("爬取失败")

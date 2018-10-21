import requests

url = "http://www.ip138.com/ips138.asp?ip="

r = requests.get(url+"110.100.1.1")
r.encoding = r.apparent_encoding
print(r.text[-5000:])
from pyquery import PyQuery as pq
import requests
import os

URL = "https://wiki.52poke.com/zh-hans/%E6%A0%91%E6%9E%9C"
r = requests.get(URL)
doc = pq(r.text)
data = doc("table").eq(1)
results = data.find("img")
ans_list = []
for i in results.items():
    ans_list.append(i)
    img = requests.get("https:" + i.attr("data-url"), stream=True)
    if img.status_code == 200:
        with open(os.path.join(os.getcwd(), "assets", "imgs") + "/" + i.attr("alt") + ".png", 'wb') as f:
            for chunk in img:
                f.write(chunk)

import requests
from bs4 import BeautifulSoup
import pandas as pd

n = int(input())

base_url = 'https://www.hanium.or.kr/portal/notice/NoticeList.do?pageIndex='
url_list=[]

for i in range(1, n+1):
    url_list.append(base_url+str(i))

titleList = []
for url in url_list:
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('a[title]')

    
    for title in titles:
        print(title.get_text())
        titleList.append(title.get_text())
    # print(titleList)

data = pd.DataFrame(titleList)
data.to_csv('2021_hanium_project_list')
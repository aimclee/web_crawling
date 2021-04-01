import urllib.request
import os
# 'https://www.topcit.or.kr/upload/edubox/essence/ess_ko_06/assets/page-images/page-523074-'
base_url = input()

# 'C:/Users/aimclee/Desktop/web_crawling/PM+techincal_communication'
path = input()

page_num = int(input())

if not os.path.isdir(path):
    os.mkdir(path)
os.chdir(path)

for i in range(1, page_num+1):
    if 1<=i<=9:
        url = base_url + '000'+ str(i)+'.jpg'
        urllib.request.urlretrieve(url,str(i)+'.jpg')
    elif 10<=i<=99:
        url = base_url + '00'+ str(i)+'.jpg'
        urllib.request.urlretrieve(url,str(i)+'.jpg')
    elif 100<=i<=999:
        url = base_url + '0'+ str(i)+'.jpg'
        urllib.request.urlretrieve(url,str(i)+'.jpg')


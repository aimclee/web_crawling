from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

chromedriver = 'C:\web_crawling\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.hanium.or.kr/portal/notice/NoticeList.do')
driver.maximize_window()

project_search = driver.find_element_by_css_selector('.boardBtn15_0603 > .powerbt')
project_search.click()
time.sleep(2)

track_s = driver.find_element_by_id("trackS")
track_s.click()
time.sleep(2)

btnSearch = driver.find_element_by_css_selector(".btn_mst4")
btnSearch.click()
time.sleep(2)


project_list_box = driver.find_elements_by_css_selector('.projectlistbox > h4 > a')
print(project_list_box)


page_strings = driver.find_elements_by_css_selector('.page_num')
print(page_strings)
page_nums=[]
for i in page_strings:
    page_nums.append(int(i.text))
print(page_nums)


action = ActionChains(driver)

titleList=[]
for j in range(1, len(page_nums)+2):
    for project in project_list_box:
        titleList.append(project.get_attribute('innerHTML'))
        action.move_to_element(project).perform
print(tuple(titleList))
        
data = pd.DataFrame(titleList)
data.to_csv('2021_smart_maritime')
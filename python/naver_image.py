from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time                                                     # 타임 package?
# import tqdm
from tqdm import tqdm                                           # 게이지 바를 시각화하여 보여주는 라이브러리

keyword = "청자켓"

# 웹 접속 - 네이버 이미지 접속
print("접속중")
driver = webdriver.Chrome('./chromedriver.exe')                 # 웹드라이버 실행
driver.implicitly_wait(30)                                      # 30초

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)

#이미지 링크 수집
imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in imgs:
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
# print(result)

driver.close()
print("수집완료")

#폴더생성
print("폴더생성")
import os
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))

print(result)
#다운로드
print("다운로드")
from urllib.request import urlretrieve
# for i in enumerate(tqdm(result)):
#     # do things
for index, link in enumerate(tqdm(result)):
    start = link.rfind('.')
    end = link.rfind('&')
    # print(link[start:end])
    filetype = link[start:end] #.png

    urlretrieve(link , './{}/{}{}{}'.format(keyword,keyword,index,filetype))

print("다운로드 완료")
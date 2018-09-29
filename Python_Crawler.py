#先嘗試將a標籤的href個別的找出來

from selenium import webdriver
from bs4 import BeautifulSoup

chrome_path = "D:\PycharmProjects\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path) #開啟Chrome瀏覽器

driver.get("https://www.ptt.cc/bbs/Beauty/M.1515902682.A.579.html")
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
image = soup.find_all("a")
for element in image:
    print(element.get('href'))
    print(len(element.get('href')))
#print(image)
driver.close()
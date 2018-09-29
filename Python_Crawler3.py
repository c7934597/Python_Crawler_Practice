#利用urllib模組的urlretrieve做下載，帶入第一個參數為URL，第二個參數為檔案名稱

from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup

chrome_path = "D:\PycharmProjects\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path) #開啟Chrome瀏覽器

driver.get("https://www.ptt.cc/bbs/Beauty/M.1515902682.A.579.html")
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)
image = soup.find_all("a")
fileName="picture"
count = 0
for element in image:
    #print(element.get('href')[len(element.get('href'))-3:len(element.get('href'))])
    if element.get('href')[len(element.get('href'))-3:len(element.get('href'))] == "jpg":
        urllib.request.urlretrieve(element.get('href'), fileName+str(count)+".jpg")
        count = count +1
        print(element.get('href'))

#print(image)
driver.close()
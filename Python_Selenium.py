from selenium import webdriver #import selenium模組
import time

chrome_path = "D:\PycharmProjects\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path) #開啟Chrome瀏覽器

time.sleep(5)

driver.get("https://www.ptt.cc/bbs/Beauty/M.1515031183.A.EB2.html") #開啟連結
elem = driver.find_element_by_link_text("https://i.imgur.com/odOG3Zr.jpg")
print(elem.text)

time.sleep(5)

driver.close() #關閉連結
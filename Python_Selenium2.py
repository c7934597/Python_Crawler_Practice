from selenium import webdriver #import selenium模組
from selenium.webdriver.common.by import By

chrome_path = "D:\PycharmProjects\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path) #開啟Chrome瀏覽器

driver.get("https://ithelp.ithome.com.tw/") #開啟連結
driver.find_element(By.XPATH,"/html/body/footer/div/div/div/ul[2]/li[2]/a").click()

driver.close() #關閉連結
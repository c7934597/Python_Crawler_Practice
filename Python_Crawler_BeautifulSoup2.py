import requests
from bs4 import BeautifulSoup
pageRequest = requests.get('http://www.cwb.gov.tw/V7/forecast/week/week.htm')

#print(pageRequest.text)

#因為亂碼，先看一下response的content
#print(pageRequest.content)

#print(pageRequest.encoding) #ISO-8859-1

soup = BeautifulSoup(pageRequest.content, 'html.parser')
soup.encoding = 'utf-8'
weather = soup.find(attrs={"class":"BoxTableInside"}).text
print(weather)
import requests
from bs4 import BeautifulSoup
pageRequest = requests.get('https://mojim.com/twy108268x5x2.htm')

soup = BeautifulSoup(pageRequest.text, 'html.parser')
song = soup.find(id='fsZx3').text

print(song)
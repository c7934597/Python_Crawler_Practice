import requests

pageRequest = requests.get('https://ithelp.ithome.com.tw/articles?tab=tech')
#print(pageRequest.headers)
#print(pageRequest.text)
#print(pageRequest.status_code)
print(pageRequest.encoding)
import requests

#year = int(input("輸入年: "))
#assert (year >= 2017), "year沒有大於等於2017"

try:
    r = requests.get('12345')
except Exception:
   print("something error happen")
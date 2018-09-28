list = [11,3,7,2,22,34,9,0,65]

def sort(listName):
  for index in range(len(listName) - 1, 0, -1):
    for secondIndex in range(index):
        if(listName[secondIndex] > listName[secondIndex + 1]):
            temp =  listName[secondIndex]
            listName[secondIndex] = listName[secondIndex + 1]
            listName[secondIndex + 1] = temp
            #print listName
  return listName

print(sort(list))

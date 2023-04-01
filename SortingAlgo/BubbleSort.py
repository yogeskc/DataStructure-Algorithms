def bubbleSort(myList): 
    for i in range(len(myList)-1, 0, -1): 
        for j in range(i): 
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList

asd=[112,34,2,13,42,1]

print(bubbleSort(asd))
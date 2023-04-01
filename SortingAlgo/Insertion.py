def BubbleSort(myList): 
    for i in range(len(myList)-1, 0 , -1): 
        for j in range(i): 
            if myList[j] > myList[j+1]: 
                temp = myList[i]
                myList[i] = myList[j+1]
                myList[j+1] = temp 
    return myList




abc = [76,123,12,34,12,21,1,0]
print(BubbleSort(abc))
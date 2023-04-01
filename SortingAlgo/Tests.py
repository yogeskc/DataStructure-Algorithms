def bubbleSort(myList): 
    for i in range(len(myList)-1,0,-1): 
        for j in range(i): 
            if myList[j] > myList[j+1]: 
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1]= temp
                
    return myList


def selectionSort(myList): 
    for i in range(len(myList)-1): 
        min_index = i 
        for j in range(i+1,len(myList)): 
            if myList[j] < myList[min_index]: 
                min_index = j 
        
        if i != min_index: 
            temp = myList[i]
            myList[i] = myList[min_index]
            myList[min_index] = temp 
    return myList
            


def insertionSort(mylist): 
    for i in range(1,len(mylist)): 
        temp = mylist[i]
        j = i -1 
        
        while temp < mylist[j] and j>-1: 
            mylist[j+1] = mylist[j]
            mylist[j]  = temp 
            j -= 1
            
    return mylist
            


print(insertionSort([121,12,3,4,33,21]))


def BubbleSort(myList): 
    for i in range(len(myList)-1, 0, -1): 
        for j in range(i): 
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
                
    return myList


def selectionSort(mylist): 
    for i in range(len(mylist)-1):
        min_index = i 
        for j in range(i+1, len(mylist) ):
            if mylist[j] < mylist[min_index]: 
                min_index = j 
        if i != min_index: 
            temp = mylist[i]
            mylist[i] = mylist[min_index]
            mylist[min_index] = temp
    return mylist
        
        
def insertion_sort(myList): 
    for i in range(len(myList)): 
        temp = myList[i]
        j = i - 1
        while temp < myList[j] and j > -1: 
            myList[j+1] = myList[j]
            myList[j] = temp
            j-=1
    return myList

abc = [15434,1454,123112,534,12312,1,123,1123]
print(insertion_sort(abc))
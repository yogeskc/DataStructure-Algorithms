def selectionSort(myList): 
    for i in range(len(myList)-1): 
        min_index = i 
        for j in range(i+1, len(myList)): 
            if myList[j] < myList[min_index]: 
                min_index = j 
        if i != min_index: 
            temp = myList[i]
            myList[i] = myList[min_index]
            myList[min_index] = temp 
            
    return myList
            
            
        
        
       
print(selectionSort([133,123,343,12423,531213,12]))
def mergeFunc(list1, list2): 
    new_list = []
    i = 0 
    j = 0 
       
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]: 
            new_list.append(list1[i])
            i +=1
        
        else: 
            new_list.append(list2[j])
            j+=1
            
    while i < len(list1):
        new_list.append(list1[i])
        i+=1
    while j < len(list2):
        new_list.append(list2[j])
        j+=1
    
    return new_list


def mergeSort(myList): 
    if len(myList) == 1: 
        return myList
    midpoin = int(len(myList)/2)
    left  = mergeSort( myList[:midpoin])
    right = mergeSort( myList[midpoin:])     
    return  mergeFunc(left, right)


originalList = [1,2,3,12,123,12,1]
sorted_list = mergeSort(originalList)

print(sorted_list)
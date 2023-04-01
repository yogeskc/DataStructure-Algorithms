def merge(list1, list2): 
    combined = []
    i = 0 
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
            
        else: 
            combined.append(list2[j])
            j+=1
            
    while i < len(list1):
            combined.append(list1[i])
            i += 1
        
    while j < len(list2):
            combined.append(list2[j])
            j+=1
            
    return combined


def mergesort(mylist): 
    if len(mylist) == 1: 
        return mylist
    mid_index = int(len(mylist)/2)
    left = mergesort(mylist[:mid_index])
    right = mergesort(mylist[mid_index:]) 
    return merge(left,right)


originalList = [1,2,3,12,123,12,1]
sorted_list = mergesort(originalList)

print(sorted_list)
def itemsCommon(list1, list2): 
    dict={}
    for i in (list1): 
        dict[i] = True
        
    for j in (list2): 
        if j in dict: 
            return True
        
    return False


list1 = {1,3,4}
list2 = {1,3,3} 

print(itemsCommon(list1, list2))
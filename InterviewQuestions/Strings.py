#Given a string, write a function to reverse the order of the words in the string.

def reverse_string(string): 
    words = string.split()
    words.reverse()
    reversed_string = " ".join(words)
    return reversed_string

#check the permutations 
def permutations(string1, string2): 
    #if the strings length are not equal they cannot be permutations of one another
    if( len(string1) != len(string2) ) : 
        return False
    
    else: 
        str1 =" ".join(sorted(string1))
        str2 =" ".join(sorted(string2))
        
        if str1 == str2 : return True
        else: return False
        
        
#check duplicates in the string 
def checkDuplicate(string): 
    unique_set = set()
    
    for char in string: 
        if char not in string:
            unique_set.add(char)
            
    uniq_char = " ".join(unique_set)
    return uniq_char
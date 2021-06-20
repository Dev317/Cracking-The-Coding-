def is_unique(string):
    if len(string) > 128:
        return False
    
    boolean_arr = [False for i in range(128)]

    for i in range(len(string)):
        index = ord(string[i])

        if boolean_arr[index] == True:
            return False
        
        boolean_arr[index] = True
    
    return True

print("Test Case: ")
print("Empty String:",is_unique(""))
print("Unique String:", is_unique("abcd"))
print("Diplication:", is_unique("abcad"))
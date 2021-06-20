def one_edit_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    long_str = None
    short_str = None
    if len(str1) > len(str2):
        long_str = str1
        short_str = str2
    else:
        long_str = str2
        short_str = str1
    
    index_long_str = 0
    index_short_str = 0
    first_diff = False

    while(index_long_str < len(long_str) and index_short_str < len(short_str)):
        if long_str[index_long_str] != short_str[index_short_str]:
            if first_diff:
                return False
            
            first_diff = True
            if (len(long_str) == len(short_str)):
                index_short_str += 1
        else:
            index_short_str += 1
        index_long_str += 1
    
    return True

print("Test Case:")
print("pale, ple ->", one_edit_away("pale", "ple"))
print("pales, pale ->",one_edit_away("pales", "pale"))
print("pale, bale ->",one_edit_away("pale", "bale"))
print("pale, bake ->", one_edit_away("pale", "bake"))
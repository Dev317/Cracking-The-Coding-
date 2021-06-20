def check_equal(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

def string_rotate(str1, str2):
    if(check_equal(str1, str2)):
        return True

    for i in range(len(str1) - 1):
        temp_str = str1[i+1:len(str1)] + str1[0:i+1]
        if (check_equal(temp_str, str2)):
            return True

    return False

print(string_rotate("waterbottle","ewaterbottl"))

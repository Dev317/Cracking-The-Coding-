def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    for i in range(len(string1)):
        curr_char = string1[i]
        check_matching = False
        for j in range(len(string2)):
            if curr_char == string2[j]:
                string2 = string2[:j] + "0" + string2[j+1:len(string2)]
                check_matching = True
                break
        
        if check_matching == False:
            return False

    return True

print("Test Case:")
print("With Empty String:", check_permutation("",""))
print("With One Single Char:", check_permutation("a", "a"))
print("With One Single Different Char:", check_permutation("a", "b"))
print("With Three Chars:", check_permutation("abc", "bac"))
print("With Repeating Chars:", check_permutation("aabbc", "bcaba"))
print("With Different Length:", check_permutation("abc", "ab"))
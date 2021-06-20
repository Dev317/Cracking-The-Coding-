def compression(string):
    if len(string) == 0:
        return ""
    
    count = 1
    result_str = string[0]
    curr_char = string[0]
    for i in range(1,len(string)):
        if string[i] != curr_char:
            result_str += str(count) + string[i]
            count = 1
            curr_char = string[i]
        else:
            count += 1
    
    result_str += str(count)
    return result_str

print("Test Case:")
print(compression("a"))
print(compression("ab"))
print(compression("aabcccccaaa"))
print(compression("AAVVDSA"))
print(compression("BBssaaEEzFd"))
print(compression(""))
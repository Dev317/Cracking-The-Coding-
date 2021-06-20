def urlify(string, replace,len):
    split = []
    stopping_index = 0
    result_str = ""
    for i in range(len):
        if string[i] == " ":
            split.append(string[stopping_index:i])
            stopping_index = i + 1

    for i in split:
        i += replace
        result_str += i

    return result_str + string[stopping_index:len]
   
string = "hello world "
replace = "%20"
len = len(string)
print(urlify(string,replace,len))
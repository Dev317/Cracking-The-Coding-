def swap(string, pos1, pos2):
    list_char = [i for i in string]
    temp_char = string[pos1]
    list_char[pos1] = list_char[pos2]
    list_char[pos2] = temp_char

    result_str = ""
    for i in list_char:
        result_str += i
    
    return result_str

#back-track
def util(string, start_index, end_index, permutation_list):
    if start_index == end_index:
        permutation_list.append(string)
        return
    else:
        for i in range(start_index, end_index + 1):
            string = swap(string, start_index, i)
            util(string, start_index + 1, end_index, permutation_list)
            string = swap(string, start_index, i)

def check_palindrome(str):
    temp_str = str[::-1]
    if str == temp_str:
        return True
    return False

string = "abb"
string = string.lower()

temp_str = ""
for i in range(len(string)):
    if string[i] != " ":
        temp_str += string[i]

permutation_list = []
util(temp_str, 0, len(temp_str) - 1, permutation_list)

valid_list = []
for i in permutation_list:
    if check_palindrome(i) == True and i not in valid_list:
        valid_list.append(i)

if len(valid_list) > 0:
    print("True", valid_list)
else:
    print("False")

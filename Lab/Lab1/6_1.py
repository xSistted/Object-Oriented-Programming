def num_to_list(num):
    try:
        num = num.replace("[", "").replace("]", "").replace(" ", "")
        num_list = list(map(int, num.split(",")))
        return num_list
    except ValueError:
        return None

def sorting_list(lst):
    return sorted(lst)

def multiplier(num_lst):
    if len(num_lst) < 2: 
        return "Invalid"

    back = num_lst[-1] * num_lst[-2]
    front = num_lst[0] * num_lst[1]

    return max(front, back)  

str_num = input()

if "[" in str_num and "]" in str_num:
    num_list = num_to_list(str_num)
    if num_list is not None:
        sorted_list = sorting_list(num_list)
        print(multiplier(sorted_list))
    else:
        print("Invalid input")
else:
    print("Invalid input")

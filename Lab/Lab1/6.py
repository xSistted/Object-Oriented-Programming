def num_to_list(num):
    num = num.replace("[", "").replace("]", "")
    num_list = num.split(",")
    print(num_list)
    # for i in num_list:
    #     if(not i.isnumeric()):
    #         return None
    try:
        num_list = list(map(int, num_list))
    except:
        return None
    return num_list

def sorting_list(lst):
    return sorted(lst)

def multiplier(num_lst):
    front = 0
    back = int(num_lst[len(num_lst)])*int(num_lst[len(num_lst)-1])
    for j in range(len(num_lst)-1, -1, -1):
        if(num_lst[j] != num_lst[-1]):
            front = int(num_lst[-1])*int(num_lst[j])
            if(back > front):
                return back
            else: 
                return front
    return "Invalid"
str_num = input()
if "[" in str_num and "]" in str_num:
    num_list = num_to_list(str_num)
    if(num_list != None):
        sorted_list = sorting_list((num_list))
        print(num_list)
        print(sorted_list)
        print(multiplier(sorted_list))
    else:
        print("Invalid")
else:
    print("Invalid")
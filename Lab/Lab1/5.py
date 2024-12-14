def make_lst(num):    
    num_list = []
    for i in num.split(" "):
        if(len(i) > 1 or not i.isnumeric()):
            print("Invalid")
            exit()
        else:
            num_list.append(int(i))
    return num_list

def sorting_lst(num_list):
    if 0 in num_list:
        not_zero = 0
        for index, value in enumerate(num_list):
            if(value != 0):
                not_zero = index
                break
        num_list[0], num_list[not_zero] = num_list[not_zero], num_list[0]
        return num_list
    else:
        return num_list

num = str(input())
num_list = make_lst(num)
num_list.sort()
sorting_lst(num_list)
num_len = len(num_list)

if(1 < num_len < 11):
    for i in num_list:
        print(i, end="")
else:
    print("Invalid")
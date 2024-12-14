def summation(n):
    sum = 0
    for i in range(1, 5):
        sum += int(n*i)
    return sum

def check(n):
    if(len(a) != 1):
        print("Invalid")
        exit()

a = input()

check(a)
print(summation(a))
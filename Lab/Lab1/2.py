def palindrome_check(n):
    pal_list = []
    for i in range(10**(int(n)-1), 10**int(n)):
        for j in range(10**(int(n)-1),10**int(n)):
            summation = str(i*j)
            if(summation == summation[::-1]):
                pal_list.append(int(summation))
    return max(pal_list)

def invalid_check(n):
    if(not n.isnumeric() or int(n) == 0 or len(n) != 1):
        return "Invalid"

digit = input()

if(invalid_check(digit) == "Invalid"):
    print(invalid_check(digit))
else:
    print(palindrome_check(digit))
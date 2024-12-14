def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def palindrome_check(n):
    max_palindrome = 0
    lower_limit = 10**(n - 1)
    upper_limit = 10**n
    for i in range(upper_limit - 1, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1): 
            product = i * j
            if product <= max_palindrome: 
                break
            if is_palindrome(product):
                max_palindrome = max(max_palindrome, product)
    return max_palindrome

def invalid_check(n):
    if not n.isdigit() or int(n) < 1:
        return "Invalid"
    return None

digit = input()

if invalid_check(digit) == "Invalid":
    print("Invalid")
else:
    print(palindrome_check(int(digit)))

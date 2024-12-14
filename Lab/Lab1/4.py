def draw_triangle(n):
    n = int(n)
    for j in range(n, 0, -1):
        print(" "*(j-1) + "#"*(n-j+1))

n = input()
draw_triangle(n)


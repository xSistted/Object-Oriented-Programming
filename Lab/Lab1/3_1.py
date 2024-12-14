import math

def park_rate(time):
    if time <= 15 * 60:
        return 0
    elif time <= 3 * 3600:
        return 10 * math.ceil(time / 3600)
    elif time <= 6 * 3600: 
        return 30 + 20 * math.ceil((time - 3 * 3600) / 3600)
    else: 
        return 200

def check_vary(a, b, c, d):
    if(not a.isnumeric() or not b.isnumeric() or not c.isnumeric() or not d.isnumeric()):
        return False
    a, b, c, d = int(a), int(b), int(c), int(d)
    if 7 <= a <= 23 and 7 <= b <= 23 and 0 <= c < 60 and 0 <= d < 60:
        if((a == 23 and c > 0) or (b == 23 and d > 0)):
            return False
        else:
            return True
    return False

h_in, m_in, h_out, m_out = input().split()

if check_vary(h_in, h_out, m_in, m_out):
    h_in, m_in, h_out, m_out = map(int, (h_in, m_in, h_out, m_out))

    time_in = h_in * 3600 + m_in * 60
    time_out = h_out * 3600 + m_out * 60
    time_range = time_out - time_in

    if time_range < 0:
        print("Invalid")
    else:
        print(park_rate(time_range))
else:
    print("Invalid")
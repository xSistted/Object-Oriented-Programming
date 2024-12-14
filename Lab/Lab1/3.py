import math

def park_rate(time):
    summ = 0
    if(time <= 15*60):
        return 0
    elif(time <= 6*3600):
        for i in range(0, 2):
            if(time >= 0):
                if(time <= 3*3600):
                    return summ + (10*math.ceil(time/3600)) 
                else:
                    summ += (20*math.ceil((time-3*3600)/3600))
                    time = time-(time-3*3600)
            else:
                break
    elif(time > 6*3600):
        return 200
    else:
        return 1
    
def check_vary(a, b, c, d):
    if(not a.isnumeric() or not b.isnumeric() or not c.isnumeric() or not d.isnumeric()):
        return 0
    elif(int(a) < 7 or int(a) > 23 or int(b) < 7 or int(b) > 23 or int(c) < 0 or int(c) > 59 or int(d) < 0 or int(d) > 59):
        return 0
    else:
        return 1

h_in, m_in, h_out, m_out = input().split(" ")

if(check_vary(h_in, h_out, m_in, m_out) != 0):
    h_in = int(h_in)
    h_out = int(h_out)
    m_in = int(m_in)
    m_out = int(m_out)

    time_in = (h_in*3600)+(m_in*60)
    time_out = (h_out*3600)+(m_out*60)
    time_range = time_out - time_in
    if(time_range < 0):
        print("Invalid")
    else:
        print(park_rate(time_range))
else:
    print("Invalid")
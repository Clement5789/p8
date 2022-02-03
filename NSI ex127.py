import random

t = [[random.randint(1,9999) for i in range(30)] for j in range(30)]
    
def maxi(t):
    mins = []
    for i in t:
        mins.append(min(i))
    
    return max(mins)

print(maxi(t))
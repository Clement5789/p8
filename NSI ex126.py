import random

t = [[random.randint(1,9999) for i in range(30)] for j in range(30)]

best = t[0][0]
for i in t:
    for j in i:
        if best < j:
            best = j

print(best)
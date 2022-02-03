m = []
for i in range(8):
    m.append([i for i in range(64)])
    
t = [i for i in range(64)]

for i in range(8):
    for j in range(8):
        t[8 * i + j] = m[i][j]
        
print(t)
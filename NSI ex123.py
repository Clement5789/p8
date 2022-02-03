t = [i for i in range(64)]
m = []
for i in range(8):
    m.append([0]*8)

for i in range(8):
    for j in range(8):
        m[i][j] = [8 * i + j]
        
print(m)
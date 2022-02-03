def nb_occurence(t, c, n):
    find = [c]*n
    for i in range(len(t) - n):
        
        if find == t[i:i + n]:
            return True
    return False
    
def grille_vide():
    return [[0 for i in range(6)] for j in range(7)]

g = grille_vide()
g[2][1] = 1
g[3][1] = 1
g[4][1] = 1
g[5][1] = 1
g[6][1] = 1


def affiche(g):
    for i in g:
        for j in i:
            if j == 0:
                print(".", end="")
            elif j == 1:
                print("X", end="")
            elif j == 2:
                print("O", end="")
        print("")
        
def coup_possible(g, c):
    if g[0][c] == 0:
        return True
    return False

def jouer(g, j, c):
    coup = j
        
    for i in range(7):
        if g[6 - i][c] == 0:
            g[6 - i][c] = coup
            break
    return g

def horiz(g, j):
    for t in g:
        if nb_occurence(t, j, 4):
            return True
    return False

def vert(g, j):
    for i in range(len(g[0])):
        col = []
        for k in g:
            col.append(k[i])
        
        if nb_occurence(col, j, 4):
            return True
    return False
            
def diag(g, j):
    for i in range(len(g) - 4):
        for i in range(len(g[0] - 4)):
            diago = g[0]
    
affiche(g)





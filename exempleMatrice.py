t = [[1,2,3,], [4,5,6]]
b = [[7,8],[9,10],[11,12]]
T = [[0,0],[0,0],[0,0]]

for i in range(len(t)):
    for j in range(len(b[0])):
        some=0
        for k in range(len(b)):
            some=some+t[i][k]*b[k][j]
            T[i][j]=some

        
print(T)


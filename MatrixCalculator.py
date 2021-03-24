def solver2X2(X):
    z=X[0][0]*X[1][1]-X[0][1]*X[1][0]
    return(z)
def solver3X3(X):
    M1=[[X[1][1],X[1][2]],[X[2][1],X[2][2]]]  
    M2=[[X[1][0],X[1][2]],[X[2][0],X[2][2]]]
    M3=[[X[1][0],X[1][1]],[X[2][0],X[2][1]]]
    Y=X[0][0]*(solver2X2(M1))- X[0][1]*(solver2X2(M2))+ X[0][2]*(solver2X2(M3))
    return Y
def solver4X4(X):
    M1=[[X[1][1],X[1][2],X[1][3]],[X[2][1],X[2][2],X[2][3]],[X[3][1],X[3][2],X[3][3]]]
    M2=[[X[1][0],X[1][2],X[1][3]],[X[2][0],X[2][2],X[2][3]],[X[3][0],X[3][2],X[3][3]]]
    M3=[[X[1][0],X[1][1],X[1][3]],[X[2][0],X[2][1],X[2][3]],[X[3][0],X[3][1],X[3][3]]]
    M4=[[X[1][0],X[1][1],X[1][2]],[X[2][0],X[2][1],X[2][2]],[X[3][0],X[3][1],X[3][2]]]
    ans= X[0][0]*solver3X3(M1)-X[0][1]*solver3X3(M2)+X[0][2]*solver3X3(M3)-X[0][3]*solver3X3(M4)
    return ans

def inputMatrix():
    X,Y=map(int,input().split())
    L=[]
    for i in range(X):
        row=list(map(int,input().split()))
        L.append(row)
    return L
L=inputMatrix()
matrix=solver4X4(L)
print(matrix)

from numpy import matrix, divide, multiply, log, ix_

def ITCC():

    f = open('teste.txt')
    XY = []
    for line in f:
        x = map(float,line.split())
        x = [y if y>0 else 0.01 for y in x]
        XY.append(x)
    M = matrix(XY)
    P = M/M.sum()
    I = information(P)

    Xc = [[0,1],[2,3]]
    Yc = [[0,1,2],[3,4,5]]

    Phat = matrix([[0.0]*len(Yc)]*len(Xc))
    for i in range(len(Xc)):
        for j in range(len(Yc)):
            Phat[i,j] = P[ ix_(Xc[i],Yc[j]) ].sum()
    Ihat = information(Phat)

    print I, Ihat, I-Ihat
    
        
def information(P):
    Px = P.sum(axis=1)
    Py = P.sum(axis=0)
    PxPy = Px*Py
    I = divide(P,PxPy)    
    I = multiply(P,log(I))

    return I.sum()

ITCC()

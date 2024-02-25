def spiral(M):
    n=len(M)
    m=len(M[0])
    S=[]
    for i in range(0,min(n//2,m//2)+1):
        for j in range(i,n-i):
            S.append(M[j][i])
        for j in range(i+1,m-i):
            S.append(M[n-1-i][j])
        for j in range(n-2-i,i-1,-1):
            S.append(M[j][m-1-i])
        for j in range(m-2-i,i,-1):
            S.append(M[i][j])
    return S

M=[["a","b","c"],["d","e","f"],["g","h","i"]]
print(spiral(M))

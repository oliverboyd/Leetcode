# https://leetcode.com/problems/spiral-matrix/

def append_if(S,M,i,j):
    n = len(M)
    m = len(M[0])
    if len(S) < n*m:
        S.append(M[i][j])

def spiral_order(M):
    n=len(M)
    m=len(M[0])
    S=[]
    for i in range(0,min(n//2,m//2)+1):
        for j in range(i,m-i):
            append_if(S,M,i,j)
        for j in range(i+1,n-i):
            append_if(S,M,j,m-1-i)
        for j in range(m-2-i,i-1,-1):
            append_if(S,M,n-1-i,j)
        for j in range(n-2-i,i,-1):
            append_if(S,M,j,i)
    return S
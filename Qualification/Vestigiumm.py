def solve(i,N,matrix,matrix_t):
    r=0
    c=0
    k=0
    for zetta in range(N):
        k=k+matrix[zetta][zetta]
        if len(list(set(matrix[zetta])))!=N:
            r=r+1
        if len(list(set(matrix_t[zetta])))!=N:
            c=c+1
    print("Case #"+str(i)+": "+str(k)+" "+str(r)+" "+str(c))

T=int(input().strip())
for i in range(1, T+1):
    matrix=[]
    N=int(input().strip())
    matrix_t=[[] for i in range(N)]
    for j in range(N):
        a=[]
        input1=input().split(" ")
        for zeta in range(N):
            e=int(input1[zeta])
            a.append(e)
            matrix_t[zeta].append(e)
        matrix.append(a)
    solve(i,N,matrix,matrix_t)
 



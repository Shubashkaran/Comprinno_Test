for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    res=1
    c=0
    i=N-1
    while i>=0:
        if A[i]==A[i-1]:
            c=c+1
            res=res*A[i]
            i=i-1
        if c==2:
            break
        i=i-1
    if c==2:
        print(res)
    else:
        print("-1")

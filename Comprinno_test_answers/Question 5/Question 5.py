for T in range(int(input())):
    N=int(input())
    L=list(map(int,input().split()))
    cnt=[L.count(-1),L.count(0),L.count(1)]
    c=len(L)-sum(cnt)
    if c>1:
        print("no")
    else:
        if c and cnt[0]:
            print("no")
        elif cnt[0]>1 and cnt[2]==0:
            print("no")
        else:
            print("yes")
            

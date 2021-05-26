for t in range(int(input())):
    n=int(input());
    l=list(map(str,input().split()))
    flag=0
    if n < 2:
        print("NO")
    else:
        for i in range(n-1):
            if l[i]=="cookie" and l[i+1]=="milk":
                #checking if bear has drank milk after eating cookie as told by his parent 
                continue
                #if bear has drank milk after eating cookie than OK
            elif l[i]=="cookie" and l[i+1]=="cookie":
                #Otherwise
                flag=1
                break; 
            else:
                #even if bear has drank only milk then OK
                pass    
        if flag==1:
            #if he as not followed his parents order
            print("NO")
        else:
            #Otherwise
            rint("YES")

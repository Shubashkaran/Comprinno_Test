import math
for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2==1 and l[0]==1 and l[n-1]==1:
        #n%2==1 checking if mid element is present or not
        #checking if 1st and last element set to 1  
        flag=1
        for i in range(n//2):
            #checking the elements till the mid element (n//2)
            if l[i]!=l[n-1-i] or l[i]!=l[i+1]-1:
                #l[i]!=l[n-1-i] checking if the left side and corresponding right side elements are not same
                #l[i]!=l[i+1]-1 checking if the elements on left side of mid value are not in increasing order by 1 and elements on right side of mid value are not in decreasing order by 1                
                flag=0
                break
                #if above conditions are true
        if flag==0:
            print("no")
            #cannot form a temple
        else:
            print("yes")
            #Otherwise
    else:
        print("no")
        #if above conditions are not met

for T in range(int(input())):
    N=input()
    L=list(map(int,input().split()))
    L2=[]
    for i in range(len(L)):
        #appending list values whose count in list L is high, so that we can use the sticks with higher length
        if L.count(L[i])>1:
            L2.append(L[i])
    #checking if there are sticks sufficient number of sticks to build a rectangle 
    if len(l2)>3:
        #Sorting and Reversing so that higher length sticks can we used first
        l2.sort()
        l2.reverse()
        #Finding the maximum possible area of the constructed rectangle
        print(l2[0]*l2[3])
    else:
        #Otherwise, it is not possible to build rectangle with given no of higher length sticks
        print('-1')

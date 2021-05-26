for T in range(int(input())):
    N=input()
    L=list(map(int,input().split()))
    L2=[]
    for i in range(len(L)):
        #appending list values whose count in list L is high to L2, so that we can use the sticks with higher length
        if L.count(L[i])>1:
            L2.append(L[i])
    #checking if there are sticks sufficient number of sticks to build a rectangle 
    if len(L2)>3:
        #Sorting and Reversing so that higher length sticks can we used first
        L2.sort()
        L2.reverse()
        #Finding the maximum possible area of the constructed rectangle
        print(L2[0]*L2[3])
    else:
        #Otherwise, it is not possible to build rectangle with given no of higher length sticks
        print('-1')

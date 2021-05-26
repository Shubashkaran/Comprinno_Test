def better(a,b):
        return (a[0]<=b[0] and a[1]<=b[1] and a[2]<=b[2]) and (a[0]<b[0] or a[1]<b[1] or a[2]<b[2])
        #1. a[0]<=b[0] and a[1]<=b[1] and a[2]<=b[2] checking if b doesn't score less than a in any of the skills
        #2. a[0]<b[0] or a[1]<b[1] or a[2]<b[2] checking if b scores more than a in atleast one of the skills
        #if both the above conditions are met than b is better person than a
for t in range(int(input())):
        S1 = list(map(int,input().split()))
        S2 = list(map(int,input().split()))
        S3 = list(map(int,input().split()))
        L=[S3,S2,S1]
        L.sort()
        #score of all the persons are added to a common list and the list is sorted
        if better(L[0],L[1]) and better(L[1],L[2]):
                #Checking if order of people exist such that i-1-th person is better than the i-th person 
                print("yes")
                #if such order exists
        else:
                print("no")
                #Otherwise
	

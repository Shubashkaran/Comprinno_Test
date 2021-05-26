#if runtime error occurs for any of input throw an exception 
try:
 for T in range(int(input())):
    s = int(input())
    lst = list(map(int, input().split()))
    #Calculate the count of -1,0,1 in list   
    a = lst.count(0)
    b = lst.count(1)
    c = lst.count(-1)
    #Find the no of values in the list which are not -1,0, or 1   
    d = s - (a+b+c)
    #For every pair of numbers ai,aj in array a, if there exist ak=ai*aj then the array is beautiful
    #checking if 
       #1. count of non -1,0,1 values are many
                    #OR
       #2. count of -1 is greater than 0 and count of non -1,0,1 values is greater than 0
                    #OR 
       #3. count of -1 is greater than 1 and count of 1 is equal to 0
    # if any one of the above condition is true than array is not beautiful
    if(d>1 or (c>0 and d>0) or (c>1 and b==0)):
        #array is not beautiful
        print('no')
    else:
        #array is beautiful
        print('yes')
except:
    pass

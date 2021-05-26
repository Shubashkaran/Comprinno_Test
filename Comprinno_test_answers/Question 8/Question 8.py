import math
for t in range(int(input())):
    a,b,n=map(int,input().split())
    c=a*(2**(math.ceil(n/2)))
    #math.ceil(n/2) is the total no turns of Alice would get.
    #final "c" is calculated by multiplying initial "a" with 2 to the power of alice turns   
    d=b*(2**(math.floor(n/2)))
    #math.floor(n/2) is the total no turns of Bob would get.
    #final "d" is calculated by multiplying initial "b" with 2 to the power of bob turns
    print(max(c,d)//min(c,d))
    #integer division of maximum number among c and d by the minimum number among c and d 

for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(min(arr)*(n-1))
    #min(arr) would give minimum value in list. Since it is the only element which is gonna be present at end.
    #n-1 is the array size when only min(arr) is present in list.
    #min(arr)*(n-1) gives the minimum sum of cost of operations needed to convert array into single element
    

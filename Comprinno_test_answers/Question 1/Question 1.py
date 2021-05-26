for T in range(int(input())):
    S=input()
    C=set(S)
    #transforming input string to a set and removing all the duplicate values in the set
    L=[]
    for i in C:
        L.append(S.count(i))
        #counting the number of occurences of each element of C in the S and append it to list L
    if len(L)<3:
        #If the number of distinct characters in the string is less than 3 i.e. |C|<3 then the string is always dynamic
        print("Dynamic")
    else:
        L.sort()
        #count list is sorted to check for the fibonacci series rule among the elements in the list 
        if L[-1]==L[-2]+L[-3]:
            #If any permutation of elements of c follows f(ci)=f(ci-1)+f(ci-2) then input string is dynamic 
            print("Dynamic")
            # if the above condition is found in the list
        else:
            print("Not")
            #Otherwise

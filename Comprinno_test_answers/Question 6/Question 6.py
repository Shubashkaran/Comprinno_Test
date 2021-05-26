for t in range(int(input())):
    cats,dogs,legs=map(int,input().split())
    m=max(dogs,cats-dogs)
    #finding maximum number of cats that can be placed on back of dogs
    if m*4<=legs and legs<=(cats+dogs)*4 and legs%4==0:
        #checking if the total legs of the maximum cats placed on back <= given leg limit
        #checking if leg count <= total count of legs (dogs and cats) and checking if any dog or cat has extra leg (legs%4)  
        print("yes")
        #if the leg count follows all the above conditions
    else:
        print("no")
        #Otherwise
    

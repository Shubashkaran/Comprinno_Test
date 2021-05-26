for T in range(int(input())):
    N=int(input());
    if N<1500: #if basic salaray is less than 1500
        HRA=10*N/100 #HRA is the 10% of the basic salary
        DA=90*N/100 #DA is the 90% of the basic salary
    else: #Otherwise
        HRA=500
        DA=98*N/100 #DA is the 98% of the basic salary
    print(N+HRA+DA) #Gross Salaray is calculated by Basic Salary+HRA+DA
        

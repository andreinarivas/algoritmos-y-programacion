number=int(input("Please enter a number: "))
aux=number-1
cont=0
if number<=1:
    print("The number is not prime")
else:
    while aux > 1:
        if number%aux==0:
            cont+=1
            break
        aux-=1
    if cont==0:
        print("The number is prime")
    else:
        print("The number is not prime")
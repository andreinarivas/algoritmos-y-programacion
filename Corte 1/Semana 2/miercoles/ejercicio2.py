number=int(input("Please enter a number: "))
aux=number-1
acum=0
while aux >= 1:
    if number%aux==0:
        acum+=aux
    aux-=1
if acum>number:
    print("The number {} is abundant".format(number))
else:
    print("The number {} is defficent".format(number))
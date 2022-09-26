number=input("Please introduce a round number: ")
full_number=int(number)
number_list=list(number)
digits=[int(x) for x in number_list]
is_complete=False
sum=0
if full_number>=10:
    while is_complete==False:
        if sum>10 or sum==0:
            sum=0
            digits=[int(x) for x in number_list]
            for x in range(0,len(digits)):
                sum+=digits[x]
            number_list=list(str(sum))
        else:
            is_complete=True
    print(sum)
else:
    print(full_number)
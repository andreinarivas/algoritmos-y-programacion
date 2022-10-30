shopping_list={}
run="yes"
total=0
while run=="yes":
    article=input('Please enter the article to buy: ')
    price=int(input('Please enter the price: \n'))
    quantity=int(input('Please enter the amount of {} to buy: '.format(article)))
    price*=quantity
    shopping_list[article]=price
    total+=price
    run=input("\n Would you like to add more articles? \n Answer 'yes' or 'no' \n >>> ")
print(shopping_list)
print(total)
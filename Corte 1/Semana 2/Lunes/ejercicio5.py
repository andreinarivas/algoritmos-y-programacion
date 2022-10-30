pizza_type=input('Please enter a valid option: \n1. vegetarian\n2.non-vegetarian \n>>')
if pizza_type=='1':
    ingredient=int(input('Available vegetarian ingredients. Choose one \n 1.Pepper \n2.Tofu \n>>'))
    if ingredient==1:
        ingredient="pepper"
    if ingredient==2:
        ingredient='tofu'
    print(f'Your pizza is vegetarian with tomato sauce, mozzarella and {ingredient}')
elif pizza_type=='2':
    ingredient=int(input('Available non-vegetarian ingredients. Choose one \n 1.Peperoni \n2.Ham \n3.Salmon \n>>'))
    if ingredient==1:
        ingredient="peperoni"
    if ingredient==2:
        ingredient='ham'
    if ingredient==3:
        ingredient="salmon"
    print(f'Your pizza is vegetarian with tomato sauce, mozzarella and {ingredient}')
else:
    print('Invalid option')
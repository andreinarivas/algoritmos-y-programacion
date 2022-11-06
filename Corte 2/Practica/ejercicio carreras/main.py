from car import Car, Race

def create_cars(cars):
  new_car=Car(
    input('Please enter the cars model: \n >>> '),
    input('Please enter the drivers name: \n >>> ')
  )
  print('\n')
  cars.append(new_car)


def main():
  cars=[]
  print('--------- WELCOME TO RACING ----------- \n Lets add the race participants! \n')  
  while len(cars)<6:
    create_cars(cars)
  race=Race(cars)
  race.start()
  race.result()

main()
import random
class Car:
  def __init__(self, brand, driver):
    self.brand=brand
    self.driver=driver


class Race:
  def __init__(self, cars:list[Car]):
    self.cars=cars


  def start(self):
    print('-RACE START-\n Participants:\n')
    for car in self.cars:
      print('*{}'.format(car.driver))
  
  def result(self):
    random.shuffle(self.cars)
    pos=1
    print('--RACE RESULT--')
    for x in self.cars:
      print('{}. {}, driving a {}'.format(pos, x.driver.capitalize, x.brand))
      pos+=1
  

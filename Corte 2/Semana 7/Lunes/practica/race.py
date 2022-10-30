import random
class Race:
  def __init__(self, horses, number):
    self.horses=horses
    self.number=number

  def race_winner(self, horses):
    winner=random.choice((self.horses)).name
    print('The race winner is {}'.format(winner))
   



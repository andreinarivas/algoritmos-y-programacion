class Vehiculo:
  def __init__(self,color, ruedas):
    self.color=color
    self.ruedas=ruedas

  def describe(self):
    print('Color: {} \n Ruedas: {}'.format(self.color, self.ruedas ))
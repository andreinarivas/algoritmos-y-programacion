from vehiculo import Vehiculo
class Coche(Vehiculo):
  def __init__(self, color, ruedas, velocidad, cilindrado):
    Vehiculo.__init__(self, color, ruedas)
    self.velocidad=velocidad
    self.cilindrado=cilindrado
 

  def describe():

    return 

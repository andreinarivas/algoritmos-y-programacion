from vehiculo import Vehiculo
class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    Vehiculo.__init__(self, color, ruedas)
    self.tipo=tipo

    
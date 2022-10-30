from vehiculo import Vehiculo
from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
  def __init__(self, color, ruedas, tipo, velocidad,cilindrada):
    Bicicleta.__init__(self, color, ruedas, tipo)
    self.velocidad=velocidad
    self.cilindrada=cilindrada

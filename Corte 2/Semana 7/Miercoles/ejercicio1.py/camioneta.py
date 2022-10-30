from vehiculo import Vehiculo
from coche import Coche

class Camioneta(Coche):
  def __init__(self, color, ruedas, velocidad, cilindrado, carga):
    Coche.__init__(self, color, ruedas, velocidad, cilindrado)
    self.carga=carga

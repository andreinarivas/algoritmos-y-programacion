class Classified:
  def __init__(self, price, publication_date, number_days, version):
    self.price=price
    self.publication_date=publication_date
    self.number_days=number_days
    self.type=version

class RealEstate(Classified):
  def __init__(self, price, publication_date, number_days, version,area,n_rooms,n_bathrooms,n_parking,law_political):
    Classified.__init__(self, price, publication_date, number_days, version)
    self.area=area
    self.n_rooms=n_rooms
    self.n_bathrooms=n_bathrooms
    self.n_parking=n_parking
    self.law_political=law_political

class Vehicle(Classified):
  def __init__(self, price, publication_date, number_days, version, brand, model,year, roadage):
    Classified.__init__(self, price, publication_date, number_days, version)
    self.brand=brand
    self.model=model
    self.year=year
    self.roadage=roadage
    

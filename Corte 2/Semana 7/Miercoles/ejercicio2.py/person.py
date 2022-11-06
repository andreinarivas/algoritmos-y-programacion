from articles import Articulo
class Person:
  def __init__(self, name, identification):
    self.name=name
    self.id=identification


class Redactor(Person):
  def __init__(self, name, identification):
    Person.__init__(self, name, identification)
  def write_article(self):
    articulo=Articulo(
      input('Title: '), input('Summary: '), input('Body: '), input(' # Images: '), input('Creation date:'), self.name)
    return articulo

class Boss(Person):
  def __init__(self, name, identification, writers):
    Person.__init__(self, name, identification)
    self.writers=writers
  def approve_article(self,article):
    pass

    

class Person:
  def __init__(self, name, identification, section):
    self.name=name
    self.id=identification
    self.section=section


class Redactor(Person):
  def __init__(self, name, identification, section):
    Person.__init__(self, name, identification, section)

class Boss(Person):
  def __init__(self, name, identification, section, writers):
    Person.__init__(self, name, identification, section)
    self.writers=writers

    

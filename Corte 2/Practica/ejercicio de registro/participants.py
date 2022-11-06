
class Participants:
  def __init__(self, name, kind, phone_number, number, category):
    self.name=name
    self.kind=kind
    self.category=category
    self.phone_number=phone_number
    self.number=number
  def print_info(self):
    for atribute, data in self.__dict__.items():
      print('{}: {}'.format(atribute, data))

class Sing(Participants):
  def __init__(self, name, kind, phone_number, number, song_name, song_author):
    Participants.__init__(self, name, kind, phone_number, number, category='Singing')
    self.song_name=song_name
    self.song_author=song_author
  

class Dance(Participants):
  def __init__(self, name, kind, phone_number, number, style):
    Participants.__init__(self, name, kind, phone_number, number, category='Dance')
    self.style=style

class Music(Participants):
  def __init__(self, name, kind, phone_number, number,instruments):
    Participants.__init__(self, name, kind, phone_number, number, category='Music',)
    self.instruments=instruments

class Free(Participants):
  def __init__(self, name, kind, phone_number, number, talent):
    Participants.__init__(self, name, kind, phone_number, number, category='Free')
    self.talent=talent



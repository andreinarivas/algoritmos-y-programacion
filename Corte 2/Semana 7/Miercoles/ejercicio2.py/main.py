from person import Person, Redactor, Boss
from articles import Articulo
from section import Section
def get_writers_section1():
  return [
    Redactor('Paula', 1235),
    Redactor('Hola', 222),
    Redactor('Gladys',1233)
  ]
def main():
 section1_boss=Boss('Jose', 123, get_writers_section1())
 section1=Section('1', section1_boss)
 print(section1.boss.name)
 for x in section1.writers:
  print(x.name)


main()
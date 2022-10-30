from race import Race
from horse import Horse
from valida import Valida
def main():

  number_validas=int(input('Please enter the number of valids you want \n >>> '))
  number_races=int(input('Please enter how many races you want for each valid \n >>> '))
  horse1=Horse('claudio', '1')

  horse2=Horse('juan', '2')

  horse3=Horse('pablo', '3')

  horse4=Horse('pedro', '4')

  horse5=Horse('gabo', '5')
  horse6=Horse('luis','6')
  for x in range(number_validas):
    races=[]
    horses=[horse1,horse2,horse3,horse4,horse5,horse6]
    for y in range(number_races):
      race=Race(horses, y)
      races.append(race)
    for race in races:
      race.race_winner(horses)


main()

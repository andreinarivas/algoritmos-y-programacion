from jugador import Player
import random

def create_player(players):
  name=input("Please enter the name of the player: \n >>> ")
  new_player=Player(name, 0)
  players.append(new_player)

def roll_dice(players, x):
  roll=random.randint(1, 6)
  print('Player {} rolled a {}'. format(players[x].name, roll))
  players[x].update_score(get_score(roll, players[x].score, players, x))
  print('Player {} has {} points'.format(players[x].name, players[x].score))


def get_score(roll, score,players, x):
  if roll==1:
    score+=10
  if roll==2:
    score+=20
  if roll==3:
    print('ROLL AGAIN')
    roll_dice(players, x)
  if roll==4:
    score*=2
  if roll==5:
    score+=40
  if roll==6:
    try:
      score/=2
    except:
      score=0
  return score



def play_round(round_number, players):
  print('------ START OF ROUND #{}------'.format(round_number))
  for x in range(len(players)):
    roll_dice(players, x)
  round_number+=1
  if round_number<8:
    play_round(round_number, players)
  else:
    print('------ END OF ROUNDS ------')
    
def get_winner(players):
  max_points=0
  winner_name=''
  winner=[]
  for x in players:
    if x.score>max_points:
      winner_name=x.name
      max_points=x.score
  winner=[winner_name,max_points]
  return winner
      



def main():
  players=[]
  add_players=True
  while add_players:
    create_player(players)
    add_players=input('Do you want to add more players? \n Yes (Y) or No (N) \n >>> ')
    if add_players=='N':
      add_players=False
  round_number=1
  play_round(round_number, players)
  print('The Winner of the game is {} with {} points'.format(get_winner(players)[0], get_winner(players)[1]))

main()
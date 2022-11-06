def move_matriz(matriz,x,y):
  read=matriz[x][y]
  if read=='WALl':
    return False
  if read=='EXIT':
    return True
  if read=='DOWN':
    x+=1
    return move_matriz(matriz, x, y)
  elif read=='UP':
    x-=1
    return move_matriz(matriz, x, y)
  elif read=='LEFT':
    y-=1
    return move_matriz(matriz, x, y)
  elif read=='RIGHT':
    y+=1
    return move_matriz(matriz, x, y)
  
  




def main():
  matriz=[
["DOWN","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
["DOWN","DOWN","LEFT","LEFT","LEFT","LEFT","LEFT"],
["DOWN","WALL","RIGHT","DOWN","DOWN","LEFT","LEFT"],
["RIGHT","RIGHT","UP","DOWN","DOWN","RIGHT","DOWN"],
["WALL","DOWN","LEFT","LEFT","RIGHT","UP","DOWN"],
["UP","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
["UP","LEFT","LEFT","LEFT","LEFT","LEFT","EXIT"],
]
  vector = [[0,0],[6,5],[2,6],[0,1]]
  for entradas in vector:
    x=entradas[0]
    y=entradas[1]
    result=move_matriz(matriz, x, y)
    if result:
      print('{} is an entrance that leads to the exit'.format(entradas))
    else:
      print('{} is not an entrance that leads to the exit'.format(entradas))

  

main()
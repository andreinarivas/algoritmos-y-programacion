#hola
saldo=3480
fecha="2020/04/10"
print(f'El saldo de la cuenta a la fecha {fecha} es ${saldo}\n')
# primera operacion
fecha='2020/04/11'
saldo-=96
print('Se han retirado $96')
print(f'El saldo de la cuenta a la fecha {fecha} es ${saldo}\n')
# segunda operacion
saldo+=1200
fecha='2020/04/17'
print('Se depositaron $1200')
print(f'El saldo de la cuenta a la fecha {fecha} es ${saldo}\n')
# tercera operacion
saldo=saldo+(saldo*0.03)
fecha='2020/04/30'
print('Se han cobrado 3% de intereses')
print(f'El saldo de la cuenta a la fecha {fecha} es ${saldo}\n')
# ultima operacion
saldo-=51
fecha='2020/05/02'
print('Se han retirado $51')
print(f'El saldo de la cuenta a la fecha {fecha} es ${saldo}')

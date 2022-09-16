chequear=input('Introduce que numero/palabra a chequear: ')
chequear_inv=(chequear[::-1])
if chequear==chequear_inv:
    print(f'{chequear} es un palindromo')
else:
    print(f'{chequear} no es un palindromo')

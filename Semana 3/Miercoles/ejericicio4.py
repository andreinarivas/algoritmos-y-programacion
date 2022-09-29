traduccion={}
data=input('Por favor introduzca las palabras del diccionario \n Debe introducirlas de modo <palabra>:<traduccion>, separando cada par por comas   \n >>> ')
pares_de_palabras=data.split(",")
palabra_espanol=[]
palabra_ingles=[]
for x in pares_de_palabras:
    palabras=x.split(":")
    palabra_espanol=palabras[0]
    palabra_ingles=palabras[1]
    traduccion[palabra_espanol]=palabra_ingles
print(traduccion)

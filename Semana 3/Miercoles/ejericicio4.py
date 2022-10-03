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
text=input('Por favor introduzca la frase a traducir: \n>>> ')
pablabras_a_traducir=text.split()
traducido=''
for x in pablabras_a_traducir:
    traducido+=traduccion.get(x,x)
    traducido+=' '
print(traducido)
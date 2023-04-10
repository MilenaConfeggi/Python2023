
frase = input("ingrese una frase ")
palabra = input("ingrese una palabra ")

palabras = frase.lower().split(' ')

cant = palabras.count(palabra)

print (cant)
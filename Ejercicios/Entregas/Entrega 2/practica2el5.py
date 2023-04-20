#from collections import Counter

# Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, 
# y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir entre
# mayúsculas y minúsculas.
def repeat():
    """ devuelve la cantidad de veces que repite una palabra dentro de la frase """
    frase = input("ingrese una frase: '")
    word = input("ingrese una palabra a buscar: '")
    lista = (frase.lower()).split()
    print(f"{word} aparece {lista.count(word.lower())}")
repeat()

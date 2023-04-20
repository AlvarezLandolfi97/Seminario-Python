from collections import Counter
texto = input("ingresa un heterograma: ")
texto.strip()
chars = list(texto.replace(" ",""))
letter_elements = set(texto.replace(" ",""))
#print(letter_elements) 
print("Es un heterogra " if len(chars) == len(letter_elements) else " No es un herograma ")  

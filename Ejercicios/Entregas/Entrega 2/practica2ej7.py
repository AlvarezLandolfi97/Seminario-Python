# Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad 
#  de palabras sin distinguir entre mayúsculas y minúsculas, en la frase.
texto = """  El salario promedio de un hombre en ARGENTINA es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.  
"""
lista = texto.split()
type_count = {"mayusculas": 0,"minusculas":0,"not_letters":0,"alpha":0}
for word in lista:
    if word.isupper():
        type_count["mayusculas"]+= 1
        type_count["alpha"]+= 1
    elif word.islower():
        type_count["minusculas"]+= 1
        type_count["alpha"]+= 1
    else:    
        type_count["not_letters"]+= 1
print(type_count)
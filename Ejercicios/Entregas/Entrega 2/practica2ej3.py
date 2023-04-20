import string
# Dado el siguiente texto guardado en la varible jupyter_info, solicite por teclado una letra e imprima las
# palabras que comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique el error. Ver:
# módulo string
jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""
palabra = input('ingrese una letra: ')
lista = jupyter_info.strip().split()
char = palabra[0]
if char in string.ascii_letters:
    for pal in lista:
        if (pal.startswith(char)):
            print(pal)
elif char in string.digits:
    print('error: se ha ingresado un numero como primer caracter')
elif char in string.punctuation:
    print('error: se ha ingresado un caracter especia como primer digito')
else:
    print('error: se ha ingresado un blanco como primer caracter')

def valor_chars():
    word = input(" ingrese una palabra ")
    if word.isalpha():
        cont = 0
        uno = frozenset("AEIOULNRST")
        dos = frozenset("DG")
        tres = frozenset("BCMP")
        cuatro = frozenset("FHVWY")
        cinco = frozenset("K")
        seis = frozenset("JX")
        siete = frozenset("QZ")
        chars = list(set(word.upper()))
        for char in chars:
            if char in uno:
                cont+=1
            elif char in dos:
                cont+=2
            elif char in tres:
                cont+=3
            elif char in cuatro:
                cont+=4
            elif char in cinco:
                cont+=5
            elif char in seis:
                cont+=6
            else:
                cont+=7
        print(f"{word} vale {cont} puntos")
    else:
        print(" No se ah ingresado letras ")
valor_chars()

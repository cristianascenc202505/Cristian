n=str(input("Introduzca una cadena de texto: "))

for l in n:
    if  not l.isalpha():
        print(f"No es una letra ({l})")
    
    else:
        print(f"Es una letra ({l})")
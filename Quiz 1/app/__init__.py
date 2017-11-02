palabra_secreta = "python"

for x in range(3):

        palabra = input("Ingresa la palabra secreta: ")
        if palabra_secreta.upper() == palabra.upper():
            print("GANASTE!!!")
            break
        elif palabra_secreta.upper() != palabra.upper() and x <= 1:
            print("Palabra incorrecta vuelva a intentarlo")
        else:
            print("Has perdido :'(")

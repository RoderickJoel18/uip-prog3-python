palabra_secreta = "python"
for x in range(3):
        palabra = input("Ingresa la palabra secreta: ")
        if palabra == palabra_secreta.upper():
            print("GANASTE!!!")
            break
        elif palabra == palabra_secreta:
            print("GANASTE!!!")
            break
        elif palabra == "Python":
            print("GANASTE!!!")
            break
        elif  palabra != palabra_secreta and x <= 1:
            print("Palabra incorrecta... Intentalo nuevamente")
        else:
            print("Has perdido...")
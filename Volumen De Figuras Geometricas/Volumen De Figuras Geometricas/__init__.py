class Figuras_Geo:

    def FEsfera(self):
        num1 = float(input("Ingrese el radio: "))
        Vol_Esfera = (4 / 3) * 3.141592 * num1 ** 3
        print("El volumen de la esfera es: ", "{0:.2f}".format(Vol_Esfera))
        print("Adios.")

    def FCilindro(self):
        num1 = float(input("Ingrese el radio: "))
        num2 = float(input("Ingrese la altura: "))
        Vol_Cilindro = 3.141592 * num1 ** 2 * num2
        print("El volumen del cilindro es:", "{0:.2f}".format(Vol_Cilindro))
        print("Adios.")

    def FCono(self):
        num1 = float(input("Ingrese el radio: "))
        num2 = float(input("Ingrese la altura: "))
        Vol_Cono = ((num1 ** 2 * num2) / 3) * 3.141592
        print("El volumen del cono es:", "{0:.2f}".format(Vol_Cono))
        print("Adios.")

class Esfera(Figuras_Geo):
        def formula(self):
            self.FEsfera()

class Cilindro(Figuras_Geo):
        def formula(self):
            self.FCilindro()

class Cono(Figuras_Geo):
        def formula(self):
            self.FCono()

if __name__ == "__main__":
    print("Opciones\n1. Esfera\n2. Cilindro\n3. Cono")
    Opcion = int(input('Introduzca la opcion que desea utilizar: '))
    try:
        if Opcion == 1:
            Esfera().formula()
        elif Opcion == 2:
            Cilindro().formula()
        elif Opcion == 3:
            Cono().formula()
    except:
        print("ERROR: Opcion Invalida.")


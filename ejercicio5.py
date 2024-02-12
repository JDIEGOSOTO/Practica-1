import random 
numero=0 
intentos=3
opcion=0
def menu():
    print("Bienvenido al menu del juego: ")
    print("1.- Generar numero aleatorio")
    print("2.- Adivinar el numero")
    print("3.- Salir")

def generar_numero():
    global numero
    numero=random.randint(1,10)
    print("Se acaba de generar un numero aleatorio del 1 al 10, su mision es adivinarlo con solo tres intentos")
def adivinar():
    global opcion
    global intentos
    intento=int(input("Intente adivinar el numero: "))
    if intento==numero:
        print("¡Felicidades usted logro adivinar el numero aleatorio!")
        opcion=3
    elif  intento<1 or intento>10:
        print("Ingrese un numero valido: ")
    else:
        intentos-=1
        if intentos==0:
            print(f"Ya no te quedan intentos el numero era: {numero}")
        elif intento<numero:
            print("El numero que ingresó es menor que el numero aleatorio")
        else:
            print("El numero que ingreso es mayor al numero aleatorio")
        print(f"Le quedan {intentos} intentos")
def salir():
    global opcion
    opcion=3
    print("Finalizar")
def validar_intentos():
    if intentos==0:
        salir()
    else:
        pass

def main():
    while True:
        menu()
        validar_intentos()
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            generar_numero()
        elif opcion==2:
            adivinar()
        elif opcion==3:
            salir()
            break
        

main()


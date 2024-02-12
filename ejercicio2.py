empleados=[]

def menu():
    print("Bienvenido al menu de opciones: ")
    print("1- Añadir empleado")
    print("2.- Eliminar empleado")
    print("3.- Mostrar empleados")
    print("4.- Buscar empleado")
    print("5.- Salario por departamento")
    print("6.- Salario general")
    print("7.- Salir")

def validar_empleados():
    if not empleados:
        print("La lista se encuentra vacía")
    else:
        menu()

def agregar_empleado():
    id=len(empleados)+1
    nombre=input("Ingrese el nombre del empleado: ")
    departamento=input("Ingrese el departamento del empleado: ")
    salario=int(input("Ingrese el salario del empleado: "))
    empleados.append((id,nombre,departamento,salario))
    print("Empleado agregado")

def eliminar_empleado():
    validar_empleados()

    print("ID\\Nombre\\Departamento\\Salario")
    for empleado in empleados:
        print(f"{empleado[0]}\t{empleado[1]}\t{empleado[2]}\t{empleado[3]}")
    
    global id

    id=int(input("Ingrese el ID del empleado a eliminar: "))
    index_id=empleados.index(id)
    del empleados[index_id]
    del empleados[index_id+1]
    del empleados[index_id+2]
    del empleados[index_id+3]
    print("Empleado eliminado")

def mostrar_empleado():
    print("ID\\Nombre\\Departamento\\Salario")
    for empleado in empleados:
        print(f"{empleado[0]}\t{empleado[1]}\t{empleado[2]}\t{empleado[3]}")

def buscar_empleados():

    print()

def salario_departamento():
    print()

def salario_general():
    print()

def salir():
    print()

def main():
    menu()
    while True:
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            agregar_empleado()
        elif opcion==2:
            eliminar_empleado()
        elif opcion==3:
            mostrar_empleado()
        elif opcion==4:
            buscar_empleados()
        elif opcion==5:
            salario_departamento()
        elif opcion==6:
            salario_general()
        elif opcion==7:
            salir()
            break
        menu()
main()  
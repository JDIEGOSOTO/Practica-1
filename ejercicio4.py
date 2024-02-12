tareas=[]
def menu():
    print("Bienvenido al menu de opciones: ")
    print("1.- Añadir tarea")
    print("2.- Eliminar tarea")
    print("3.- Mostrar todas las tareas")
    print("4.- Marcar tarea como completada")
    print("5.- Salir")

def agregar_tarea():
    print("Añadiendo tarea")
    tarea=input("Ingrese el nombre de la tarea a añadir: ")
    tarea+=" (Pendiente)"
    tareas.append(tarea)
    print("Tarea añadida :)")

def eliminar_tarea():
    if not tareas:
        print("No hay tareas en el administrador de tareas")
        return
    print("Lista de tareas: ")
    for tarea in tareas:
        print(f"- {tarea}")
    buscar_eliminar=input("Ingrese el nombre de la tarea a eliminar: ")
    buscar_eliminar2=buscar_eliminar+" (Pendiente)"
    buscar_eliminar3=buscar_eliminar+" (Completado)"
    if buscar_eliminar2 in tareas:
        tareas.remove(buscar_eliminar2)
        print(f"Elemento {buscar_eliminar} eliminado del administrador de tareas")
        print("Lista actualizada: ")
        for tarea in tareas:
            print(f"- {tarea}")
    elif buscar_eliminar3 in tareas:
        tareas.remove(buscar_eliminar3)
        print(f"Elemento {buscar_eliminar} eliminado del administrador de tareas")
        print("Lista actualizada: ")
        for tarea in tareas:
            print(f"- {tarea}")
    else: 
        print("Elemento no encontrado")
         
def mostrar_tarea():
    print("Lista de tareas: ")
    for tarea in tareas:
        print(f"- {tarea}")

def marcar_tarea_finalizada():
    print("Lista de tareas: ")
    for tarea in tareas:
        print(f"- {tarea}")
    marcar_tarea1=input("Ingrese el nombre de la tarea a marcar: ")
    marcar_tarea2=marcar_tarea1+" (Pendiente)"
    if marcar_tarea2 in tareas:
        indice=tareas.index(marcar_tarea2)
        tareas[indice]=marcar_tarea1+" (Completado)"
    else:
        print("Elemento no encontrado")
    print("Lista actualizada: ")
    for tarea in tareas:
        print(f"- {tarea}")
      
def salir():
    print("Finalizando")

def main():
    menu()
    while True:
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            agregar_tarea()
        elif opcion==2:
            eliminar_tarea()
        elif opcion==3:
            mostrar_tarea()
        elif opcion==4:
            marcar_tarea_finalizada()
        elif opcion==5:
            salir()
            break
        else:
            print("Ingrese una opcion valida")
        menu()

main()

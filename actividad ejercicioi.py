import os
import msvcrt

while True:
    print ("<<Press Any Key>>")
    msvcrt.getch()
    os.system("cls")
    print("""
    Sistema gimnasio
    =================
    1) Registrar un nuevo usuario.
    2) Reservar una clase
    3) Consultar clases disponibles
    4) Consultar reservas de un usuario.   
    0) Salir del programa  """)
    opcion = int(input("Seleccione : "))
    
    if opcion==0:
        break
    elif opcion==1:
        print("Registrar un nuevo usuario")
        nombre = input("Ingrese nombre del usuario para registrar")
    elif opcion==2:
        print("Reservar una clase")
    elif opcion==3:
        print("Consultar clases disponibles")
    elif opcion==4:
        print("Consultar reservas de un usuario")
    else:
        print("Opcion no valida")

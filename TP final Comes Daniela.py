import os
Paquetes= {
    "Ushuaia + Calafate": "$ 1.000.000, 10 unidades",
    "Salta": "$500.000, 10 unidades",
    "Mendoza + San Rafael": "$ 800.000, 10 unidades",}

#Agregar y eliminar un producto al inventario:
def Agregar():
    nombre= input("Ingrese el nombre de un producto: ")
    precio= float(input("Ingrese el precio del producto: "))
    cantidad= int(input("Ingrese una cantidad: "))    
    Paquetes[nombre]= {"Precio": precio, "Cantidad": cantidad}
    print("Producto agregado.")
    print("1. Sí")
    print("0. No")
    opcion= int(input("¿Desea agregar otro producto? "))
    if opcion==1:
        Agregar()
    elif opcion==0:
        Menu()
    else:
        print("Opción incorrecta.")
    
def Eliminar():
    nombre= input("Ingrese el nombre de un producto: ")
    del Paquetes[nombre]
    print("Producto eliminado.")
    print("1. Sí")
    print("0. No")
    opcion= int(input("¿Desea eliminar otro producto? "))
    if opcion==1:
        Eliminar()
    elif opcion==0:
        Menu()
    else:
        print("Opción incorrecta.")

#Lista de productos:
def Lista():
    sorted(Paquetes.keys())
    print(Paquetes)
    Menu()

#Buscar un producto:
def Buscar():
    producto= input("Ingrese el nombre del producto: ")
    if producto in Paquetes:
        print(f"{producto}: {Paquetes[producto]}")
    else:
        print(f"{producto} no se encuentra en la lista.")
    Menu()

#Actualizar la cantidad de un producto:
def Actualizar():
    nombre= input("Ingrese el nombre de un producto: ")
    cantidad= (input("Ingrese una cantidad: "))
    if nombre in Paquetes:
        Paquetes[nombre]= cantidad
        print(Paquetes)
    else:
        print("Error")
    Menu()

#Salir del menú:
def Salir():
    print("¡Gracias por elegirnos!")

#Menu:
def Menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Listar productos")
    print("4. Buscar producto")
    print("5. Actualizar cantidad")
    print("6. Salir")
    seleccion= int(input("Ingrese una opción: "))
    while True:
        if seleccion==1:
            Agregar()
            break
        elif seleccion==2:
            Eliminar()
            break
        elif seleccion==3:
            Lista()
            break
        elif seleccion==4:
            Buscar()
            break
        elif seleccion==5:
            Actualizar()
            break
        elif seleccion==6:
            Salir()
            break
        else:
            print("Opción inválida.")
            break
Menu()
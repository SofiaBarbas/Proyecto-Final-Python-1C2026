import sqlite3
from colorama import Fore, init

#para inicilaizar colorama y que los colores se reinicien automáticamente después de cada print
init(autoreset=True)

def agregarProductos():
    print("\n---Agregá Productos para Registrar---")
    while True:
        nombre = input("Nombre (Tocá Enter para terminar): ").strip()
        if nombre == "": break
        
        categoria = input("Categoría (Tocá Enter para terminar): ").strip()
        if categoria == "": break
        
        # para validar que el precio sea número
        try:
            precio = int(input("Precio (debe ser un numero entero): "))
        except ValueError:
            print("[ERROR] El precio debe ser un número entero\n")
            continue

        # cada producto será un diccionario
        unProducto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }

        #los productos totales serán una lista de diccionarios
        productos.append(unProducto)

        print(Fore.GREEN + f"Producto [{nombre}] agregado exitosamente\n")


def mostrarProductos():
    print("\n---Mostrando Productos Registrados---")

    #si no hay productos, unicamente muestra mensaje
    if not productos:
        print(Fore.RED + "No hay productos para mostrar")
        return None

    for producto in productos:
        indice = productos.index(producto)+1
        print(Fore.GREEN + f"Producto {indice}:\n Nombre: {producto["nombre"]}\n Categoria: {producto['categoria']}\n Precio: {producto['precio']}")
    

def eliminarProducto():
    print("\n---Eliminá Productos Registrados---")
    
    mostrarProductos()
    if not productos:
        return None
    
    while True:
        try:
            numero = int(input("Escribí el número del producto a eliminar: "))
            if (1 <= numero <= len(productos)):
                eliminado = productos.pop(numero - 1)
                print(Fore.GREEN + f"Producto [{eliminado["nombre"]}] eliminado exitosamente")
                break
            else:
                print(Fore.RED + "El número está fuera de rango.")
        except ValueError:
            print(Fore.RED + "El numero no es válido. Debe ser un entero.")
     

def buscarProducto():
    print("\n---Buscá Productos Registrados---")
    
    if not productos:
        print(Fore.RED + "No hay productos para buscar")
        return None
    
    nombre = input("Escribí el nombre del producto que querés buscar: ")
    
    productoEncontrado = None
    for producto in productos:
        if(producto["nombre"] == nombre):
            productoEncontrado = producto
            break
    
    if(productoEncontrado):
        print(Fore.GREEN + f"El producto ha sido encontrado y es {productoEncontrado}")
    else:
        print(Fore.RED + "El producto no existe")


def calcularEleccion(eleccion):
    match(eleccion):
        case 1:
            agregarProductos()
        case 2:
            mostrarProductos()
        case 3:
            eliminarProducto()
        case 4:
            buscarProducto()
        case 5:
            print(Fore.GREEN + "Decidiste salir del programa")
        case _:
            print(Fore.RED + "Escribiste un valor no valido")


#main()
productos = []
print("---Bienvenidos al Sistema de Gestión de Productos---")
while True:
    print("\n---Menu---")
    print("Elegí la opción que quieras realizar:")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Eliminar productos")
    print("4. Buscar producto")
    print("5. Salir")
    try:
        eleccion = int(input("\nElijo la opción "))
    except ValueError:
        print(Fore.RED + "[ERROR] El valor ingresado no inválido. Por favor, ingresá un número del 1 al 5")
        continue
    calcularEleccion(eleccion)
    if(eleccion == 5):
        break
print("Hasta la proxima\n")

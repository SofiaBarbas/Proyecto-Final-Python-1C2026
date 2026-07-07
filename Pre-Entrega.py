def tocoEnter(valor):
    if (valor == ""):
        return True
    return False


def agregarProductos():
    print("\n---Agregá Productos para Registrar---")
    while True:
        print("Ingresa datos del producto (toca Enter en cualquiera para finalizar)")
        nombre = input("Ingresa el nombre: ")
        categoria = input("Ingresa la categoria: ")
        precio = int(input("Ingresa el precio: "))
        if(tocoEnter(nombre) or tocoEnter(categoria) or tocoEnter(precio)):
            break

        #diccionario
        unProducto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }

        #lista de diccionarios
        productos.append(unProducto)


def mostrarProductos():
    print("\n---Mostrando Productos Registrados---")

    if(len(productos) == 0):
        print("No hay productos para mostrar")
        return None

    for producto in productos:
        indice = productos.index(producto)+1
        print(f"Producto {indice}:\n Nombre: {producto["nombre"]}\n Categoria: {producto['categoria']}\n Precio: {producto['precio']}")
    

def eliminarProducto():
    print("\n---Eliminá Productos Registrados---")
    
    if(len(productos) == 0):
        print("No hay productos para eliminar")
        return None
     
    while True:
        numero = int(input("Escribí el número del producto a eliminar: "))
        if(numero <= 0):
            print("Numero de Producto invalido. Debe ser mayor a 0") 
        elif(numero <= len(productos)):
            productos.pop((numero-1))
            print("El producto ha sido eliminado")
            return None
        else:    
            print("No hay tantos productos. Elegi uno valido")  
        

def buscarProducto():
    print("\n---Buscá Productos Registrados---")
    
    if(len(productos) == 0):
        print("No hay productos para buscar")
        return None
    
    nombre = input("Escribí el nombre del producto que querés buscar: ")

    for producto in productos:
        if(producto["nombre"] == nombre):
            productoEncontrado = producto
            break
    
    if(productoEncontrado):
        print(f"El producto ha sido encontrado y es {productoEncontrado}")
    else:
        print("El producto no existe")


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
            print("Decidiste salir del programa")
        case _:
            print("Escribiste un valor no valido")


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
    eleccion = int(input("\nElijo la opción "))
    calcularEleccion(eleccion)
    if(eleccion == 5):
        break
print("Hasta la proxima")

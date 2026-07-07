import sqlite3
from colorama import Fore, init

#para inicilaizar colorama y que los colores se reinicien automáticamente después de cada print
init(autoreset=True)


def inicializarBaseDeDatos():
    """Crea la base de datos 'inventario.db' y la tabla 'productos' """
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        ''')
        conexion.commit()
        conexion.close()

    #por si sucede un error con la base de datos
    except sqlite3.Error as e: 
        print(Fore.RED + f"Error al inicializar la base de datos: {e}")



def verificarSiHayProductos():
    """Función auxiliar para reutilizar lógica de chequeo"""
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT count(*) FROM productos")
    cantidad = cursor.fetchone()[0]
    conexion.close()
    return cantidad > 0



def registrarProducto():
    print(Fore.CYAN + "\n--- Registrar Nuevo Producto ---")
    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        categoria = input("Categoría: ").strip()
        
        if not nombre or cantidad < 0 or precio < 0:
            print(Fore.RED + "Los datos son inválidos")
            return
        
        #si todo sale bien
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)", 
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        conexion.close()
        print(Fore.GREEN + "Producto registrado con éxito")

    except ValueError:
        print(Fore.RED + "[ERROR] La cantidad y el precio deben ser números.")



def listarProductos():
    """Muestra todos los productos"""
    print(Fore.CYAN + "\n--- Mostrando Inventario ---")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    ##si la lista está vacía
    if not verificarSiHayProductos():
        print(Fore.RED + "No hay productos para mostrar")
    else:
        for producto in productos:
            print(f"ID: {producto[0]}\n Nombre: {producto[1]}\n Cantidad: {producto[3]}\n Precio: ${producto[4]}\n Categoria: {producto[5]}\n")
        conexion.close()



def actualizarProducto():
    """Actualiza cantidad o precio por ID"""
    print(Fore.CYAN + "\n--- Actualizar Producto ---")
    
    if not verificarSiHayProductos():
        print(Fore.RED + "No hay productos para actualizar")
        return
    
    idProducto = input("ID del producto a actualizar: ")
    nuevaCantidad = int(input("Indique la nueva cantidad: "))
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nuevaCantidad, idProducto))
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + "Producto actualizado")



def eliminarProducto():
    """Elimina un producto por ID"""
    print(Fore.CYAN + "\n--- Eliminar Producto ---")

    if not verificarSiHayProductos():
        print(Fore.RED + "No hay productos para eliminar")
        return
    
    idProducto = input("ID del producto a eliminar: ")
    confirmar = input(Fore.YELLOW + f"¿Confirmas eliminar el producto {idProducto}? (s/n): ")
    if confirmar.lower() == 's':
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (idProducto,))
        conexion.commit()
        conexion.close()
        print(Fore.GREEN + "Producto eliminado")
    else:
        print(Fore.YELLOW + "Eliminación cancelada")
     


def reporteDeStock():
    """Lista productos con stock bajo"""
    print(Fore.CYAN + "\n---  Generar Reporte de Stock ---")
    
    limite = int(input("Busca productos con una Cantidad menor o igual a: "))
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    resultados = cursor.fetchall()

    if not resultados:
        print(Fore.RED + "No hay productos con esa cantidad en stock")
    else:
        print(Fore.GREEN + f"\nProductos con stock <= {limite}:")
        for producto in resultados:
            print(f"De {producto[1]} (ID: {producto[0]}) hay {producto[3]} unidades")
        conexion.close()



def calcularEleccion(eleccion):
    match(eleccion):
        case 1:
            registrarProducto()
        case 2:
            listarProductos()
        case 3:
            actualizarProducto()
        case 4:
            eliminarProducto()
        case 5:
            reporteDeStock()
        case 6:
            print(Fore.CYAN + "\n--- Decidiste salir del programa ---")
        case _:
            print(Fore.RED + "Escribiste un valor no valido")



#cuerpom del main()
inicializarBaseDeDatos()
print(Fore.CYAN + "\n--- Bienvenidos al Sistema de Gestión de Inventario ---")
while True:
    print(Fore.CYAN + "\n--- Menu ---")
    print("Elegí la opción que quieras realizar:")
    print("1. Registrar productos")
    print("2. Listar productos")
    print("3. Actualizar productos")
    print("4. Eliminar un producto")
    print("5. Generar reporte de stock")
    print("6. Salir")
    try:
        eleccion = int(input("\nElijo la opción "))
    except ValueError:
        print(Fore.RED + "[ERROR] El valor ingresado no inválido. Por favor, ingresá un número del 1 al 5")
        continue
    calcularEleccion(eleccion)
    if(eleccion == 6):
        break
print(Fore.CYAN + "Hasta la proxima\n")

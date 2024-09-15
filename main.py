"""
Programa para buscar las cantidad vendidas de un producto
"""

ventas = [("Laptops", 3), ("Celulares", 5), ("Monitores", 2), ("Teclados", 4)]

while True:
    consulta = input("Ingrese el producto a consultar: ").strip()  # Eliminamos espacios en blanco
    PRODUCTO_ENCONTRADO = False  # Corregido para cumplir con la convención de nombres

    for producto, cantidad in ventas:
        if producto.lower().startswith(consulta.lower()):  # Búsqueda insensible a mayúsculas
            print(f"El total de {producto} vendido fue {cantidad}")
            PRODUCTO_ENCONTRADO = True  # Cambiado para conformar la convención de nombres
            break  # Salimos del for cuando encontramos el producto

    if PRODUCTO_ENCONTRADO:
        break  # Salimos del while cuando la consulta es válida

    print("Producto no encontrado. Intente de nuevo.")  # Eliminado el else innecesario
    
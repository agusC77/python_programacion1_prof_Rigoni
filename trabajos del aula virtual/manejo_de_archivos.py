#actividad 1: generamos el archivo del gestor de productos
with open("productos.txt","w",encoding="utf-8") as archivo:
    archivo.write("nombre, precio, cantidad \n")
    archivo.write("lapicera, 1000.99 ,15 \n")
    archivo.write("cuaderno, 5466, 10 \n")
    archivo.write("auto, 5000000,5 \n")

#actividad 2: cargar los productos en una lista y mostrarlos y actividad 4: cargar los productos en una lista de diccionarios

productos = []
with open("productos.txt","r",encoding="utf-8") as archivo:
    for linea in archivo:
        nombre,precio,cantidad = linea.strip().split(",")
        producto = {"nombre":nombre,"precio":precio,"cantidad": cantidad}
        productos.append(producto)

print("=== Lista de productos ===")
for i in productos:
    print(f"Producto: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")
print()

#actividad 3: agregar producto, con su precio y su cantidad

nuevo_producto = input("ingrese el nombre del nuevo producto: ").strip()
nuevo_precio = float(input("ingrese el precio del nuevo producto: "))
nueva_cantidad = int(input("ingrese la cantidad del nuevo producto: "))

producto = {"nombre":nuevo_producto,"precio":nuevo_precio,"cantidad": nueva_cantidad}
productos.append(producto)
print("producto agregado con exito")

#actividad 5: buscar un producto en la lista

producto_buscado = input("ingrese el nombre del producto a buscar: ")
encontrado = False

for i in productos:
    if i["nombre"].lower() == producto_buscado.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {i['nombre']}")
        print(f"Precio: {i['precio']}")
        print(f"Cantidad: {i['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n Producto no encontrado.")

#actividad 6: sobreescribir el archivo con la nueva lista de productos

with open("productos.txt","w",encoding = "utf-8") as archivo:
    for i in productos:
        archivo.write(f"{i['nombre']},{i['precio']},{i['cantidad']}\n")

print("archivo sobreescrito correctamente")
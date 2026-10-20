"""Sistema básico de inventario de productos con programación orientada a objetos."""


class Producto:
    """Representa un producto y valida su estado antes de guardarlo."""

    def __init__(self, nombre, precio, cantidad):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto.")
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero.")

        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio después de validar el nuevo valor."""
        if isinstance(nuevo_precio, bool) or not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza las existencias después de validar el nuevo valor."""
        if isinstance(nueva_cantidad, bool) or not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """Devuelve el valor de las existencias de este producto."""
        return self.precio * self.cantidad

    def __str__(self):
        """Devuelve un resumen legible del producto."""
        return (
            f"{self.nombre} | Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad} | Valor: ${self.calcular_valor_total():.2f}"
        )


class Inventario:
    """Administra una colección de productos."""

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Añade un objeto Producto al inventario."""
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        """Busca por nombre exacto sin distinguir mayúsculas y minúsculas."""
        if not isinstance(nombre, str):
            raise TypeError("El nombre de búsqueda debe ser texto.")
        nombre_busqueda = nombre.strip().lower()
        if not nombre_busqueda:
            raise ValueError("El nombre de búsqueda no puede estar vacío.")

        for producto in self.productos:
            if producto.nombre.lower() == nombre_busqueda:
                return producto
        return None

    def calcular_valor_inventario(self):
        """Suma el valor total de todos los productos."""
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total

    def listar_productos(self):
        """Muestra todos los productos o informa que no hay existencias."""
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\nProductos en inventario:")
        for numero, producto in enumerate(self.productos, start=1):
            print(f"{numero}. {producto}")


def menu_principal(inventario=None):
    """Muestra el menú y procesa operaciones hasta que se elija salir."""
    if inventario is None:
        inventario = Inventario()

    while True:
        print("\n=== Sistema de inventario ===")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: ").strip().replace(",", "."))
                cantidad = int(input("Cantidad: ").strip())
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print(f"Producto agregado: {producto}")
            except (ValueError, TypeError) as error:
                print(f"No se agregó el producto: {error}")

        elif opcion == "2":
            try:
                nombre = input("Nombre exacto del producto: ")
                producto = inventario.buscar_producto(nombre)
                if producto is None:
                    raise LookupError(f"No existe un producto llamado '{nombre.strip()}'.")
                print(producto)
            except (ValueError, TypeError, LookupError) as error:
                print(f"No se pudo completar la búsqueda: {error}")

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: ${total:.2f}")

        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)





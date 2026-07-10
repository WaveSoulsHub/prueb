juegos = {
    "G001": ["Eclipse Runner", "PC", "accion", "T", True, "NovaStudio"],
    "G002": ["Puzzle Atlas", "Switch", "puzzle", "E", False, "BrightWorks"],
    "G003": ["Sky Legends", "PS5", "aventura", "T", True, "OrionGames"],
    "G004": ["Racing Pulse", "PC", "carreras", "E", True, "VelocityLab"],
    "G005": ["Mystic Farm", "Switch", "simulacion", "E", False, "GreenSeed"],
    "G006": ["Shadow Tactics", "Xbox", "estrategia", "M", False, "IronGate"]
}

inventario = {
    "G001": [9990, 7],
    "G002": [19990, 0],
    "G003": [42990, 3],
    "G004": [14990, 5],
    "G005": [17990, 9],
    "G006": [39990, 2]
}


def validar_texto(texto):
    return texto.strip() != ""


def validar_codigo(codigo, juegos):
    codigo = codigo.strip().upper()
    return codigo != "" and codigo not in juegos


def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.strip().upper()
    return clasificacion in ["E", "T", "M"]


def validar_multiplayer(multiplayer):
    multiplayer = multiplayer.strip().lower()
    return multiplayer in ["s", "n"]


def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return stock >= 0


def buscar_codigo(codigo, inventario):
    codigo = codigo.strip().upper()
    return codigo in inventario


def stock_plataforma(plataforma, juegos, inventario):

    total_stock = 0

    for codigo in juegos:

        plataforma_juego = juegos[codigo][1]

        if plataforma_juego.lower() == plataforma.lower():
            total_stock += inventario[codigo][1]

    print("El total de stock disponibles es:", total_stock)


def busqueda_precio(p_min, p_max, juegos, inventario):

    lista_juegos = []

    for codigo in inventario:

        precio = inventario[codigo][0]
        stock = inventario[codigo][1]

        if precio >= p_min and precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            lista_juegos.append(titulo + "--" + codigo)

    lista_juegos.sort()

    if len(lista_juegos) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print("Los juegos encontrados son:")
        print(lista_juegos)


def actualizar_precio(codigo, nuevo_precio, inventario):

    codigo = codigo.strip().upper()

    if buscar_codigo(codigo, inventario):
        inventario[codigo][0] = nuevo_precio
        return True

    return False


def agregar_juego(codigo, titulo, plataforma, genero,
                  clasificacion, multiplayer, editor,
                  precio, stock, juegos, inventario):

    codigo = codigo.strip().upper()

    if codigo in juegos:
        return False

    juegos[codigo] = [
        titulo,
        plataforma,
        genero,
        clasificacion,
        multiplayer,
        editor
    ]

    inventario[codigo] = [
        precio,
        stock
    ]

    return True


def eliminar_juego(codigo, juegos, inventario):

    codigo = codigo.strip().upper()

    if buscar_codigo(codigo, inventario):

        del juegos[codigo]
        del inventario[codigo]

        return True

    return False


def leer_opcion():

    while True:

        try:
            opcion = int(input("Ingrese opción: "))

            if opcion >= 1 and opcion <= 6:
                return opcion

            print("Debe seleccionar una opción válida")

        except:
            print("Debe ingresar un número entero")


while True:

    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()


    if opcion == 1:

        plataforma = input("Ingrese plataforma a consultar: ")
        stock_plataforma(plataforma, juegos, inventario)


    elif opcion == 2:

        while True:

            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))

                if precio_min >= 0 and precio_max >= 0 and precio_min <= precio_max:
                    break

                print("Debe ingresar valores válidos")

            except:
                print("Debe ingresar valores enteros")

        busqueda_precio(precio_min, precio_max, juegos, inventario)


    elif opcion == 3:

        continuar = "s"

        while continuar == "s":

            codigo = input("Ingrese código del juego: ")

            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))

                if nuevo_precio <= 0:
                    print("El precio debe ser mayor a cero")

                else:

                    if actualizar_precio(codigo, nuevo_precio, inventario):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")

            except:
                print("Debe ingresar un número entero")

            while True:

                continuar = input(
                    "¿Desea actualizar otro precio (s/n)?: "
                ).strip().lower()

                if continuar in ["s", "n"]:
                    break

                print("Debe ingresar s o n")


    elif opcion == 4:

        codigo = input("Ingrese código del juego: ")
        titulo = input("Ingrese título: ")
        plataforma = input("Ingrese plataforma: ")
        genero = input("Ingrese género: ")
        clasificacion = input("Ingrese clasificación: ")
        multiplayer = input("¿Es multiplayer? (s/n): ")
        editor = input("Ingrese editor: ")

        try:

            precio = int(input("Ingrese precio: "))
            stock = int(input("Ingrese stock: "))

            if not validar_codigo(codigo, juegos):
                print("Código inválido o ya existente")

            elif not validar_texto(titulo):
                print("Título inválido")

            elif not validar_texto(plataforma):
                print("Plataforma inválida")

            elif not validar_texto(genero):
                print("Género inválido")

            elif not validar_clasificacion(clasificacion):
                print("Clasificación inválida")

            elif not validar_multiplayer(multiplayer):
                print("Debe ingresar s o n en multiplayer")

            elif not validar_texto(editor):
                print("Editor inválido")

            elif not validar_precio(precio):
                print("Precio inválido")

            elif not validar_stock(stock):
                print("Stock inválido")

            else:

                multiplayer_bool = multiplayer.strip().lower() == "s"

                if agregar_juego(
                        codigo,
                        titulo.strip(),
                        plataforma.strip(),
                        genero.strip(),
                        clasificacion.strip().upper(),
                        multiplayer_bool,
                        editor.strip(),
                        precio,
                        stock,
                        juegos,
                        inventario):

                    print("Juego agregado")

                else:
                    print("El código ya existe")

        except:
            print("Precio y stock deben ser números enteros")


    elif opcion == 5:

        codigo = input("Ingrese código del juego: ")

        if eliminar_juego(codigo, juegos, inventario):
            print("Juego eliminado")
        else:
            print("El código no existe")


    elif opcion == 6:
        print("Programa finalizado.")
        break
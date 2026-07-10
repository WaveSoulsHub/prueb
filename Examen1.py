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


def valid_text(texto):
    return texto.strip() != ""


def valid_cod(codigo, juegos):
    codigo = codigo.strip().upper()
    return codigo != "" and codigo not in juegos


def valid_clasif(clasificacion):
    clasificacion = clasificacion.strip().upper()
    return clasificacion in ["E", "T", "M"]


def calid_multi(multiplayer):
    multiplayer = multiplayer.strip().lower()
    return multiplayer in ["si", "no"]


def valid_prec(precio):
    return precio > 0


def valid_stock(stock):
    return stock >= 0


def busc_codigo(codigo, inventario):
    codigo = codigo.strip().upper()
    return codigo in inventario


def stock_plat(plataforma, juegos, inventario):

    tot_stock = 0

    for codigo in juegos:

        plat_juego = juegos[codigo][1]

        if plat_juego.lower() == plataforma.lower():
            tot_stock += inventario[codigo][1]

    print("El total de stock disponibles es:", tot_stock)


def busq_prec(p_min, p_max, juegos, inventario):

    list_juegos = []

    for codigo in inventario:

        precio = inventario[codigo][0]
        stock = inventario[codigo][1]

        if precio >= p_min and precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            list_juegos.append(titulo + "--" + codigo)

    list_juegos.sort()

    if len(list_juegos) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print("Los juegos encontrados son:")
        print(list_juegos)


def act_prec(codigo, nuev_prec, inventario):

    codigo = codigo.strip().upper()

    if busc_codigo(codigo, inventario):
        inventario[codigo][0] = nuev_prec
        return True

    return False


def agreg_juego(codigo, titulo, plataforma, genero,
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


def elimi_juego(codigo, juegos, inventario):

    codigo = codigo.strip().upper()

    if busc_codigo(codigo, inventario):

        del juegos[codigo]
        del inventario[codigo]

        return True

    return False


def leer_opc():

    while True:

        try:
            opc = int(input("Ingrese una opcion: "))

            if opc >= 1 and opc <= 6:
                return opc

            print("Debe seleccionar una opcion valida")

        except:
            print("Debe ingresar un numero entero")


while True:

    print("(Menu)")
    print("(1) Stock por plataforma")
    print("(2) Busqueda de juegos por rango de precio")
    print("(3) Actualizar precio de juego")
    print("(4) Agregar juego")
    print("(5) Eliminar juego")
    print("(6) Salir")
    print("---------------------------------------")

    opc = leer_opc()


    if opc == 1:

        plataforma = input("Ingrese la plataforma a consultar: ")
        stock_plat(plataforma, juegos, inventario)


    elif opc == 2:

        while True:

            try:
                prec_min = int(input("Ingrese precio minimo: "))
                prec_max = int(input("Ingrese precio maximo: "))

                if prec_min >= 0 and prec_max >= 0 and prec_min <= prec_max:
                    break

                print("Debe ingresar valores validos")

            except:
                print("Debe ingresar valores enteros")

        busq_prec(prec_min, prec_max, juegos, inventario)


    elif opc == 3:

        continuar = "si"

        while continuar == "si":

            codigo = input("Ingrese codigo del juego: ")

            try:
                nuev_prec = int(input("Ingrese nuevo precio: "))

                if nuev_prec <= 0:
                    print("El precio debe ser mayor a cero")

                else:

                    if act_prec(codigo, nuev_prec, inventario):
                        print("Precio actualizado")
                    else:
                        print("El codigo no existe")

            except:
                print("Debe ingresar un numero entero")

            while True:

                continuar = input(
                    "¿Desea actualizar otro precio (si/no)?: "
                ).strip().lower()

                if continuar in ["si", "no"]:
                    break

                print("Debe ingresar (si) o (no)")


    elif opc == 4:

        codigo = input("Ingrese el codigo del juego: ")
        titulo = input("Ingrese su titulo: ")
        plataforma = input("Ingrese la plataforma: ")
        genero = input("Ingrese el genero: ")
        clasificacion = input("Ingrese su clasificacion: ")
        multiplayer = input("Es multiplayer? (si/no): ")
        editor = input("Ingrese el editor: ")

        try:

            precio = int(input("Ingrese precio: "))
            stock = int(input("Ingrese stock: "))

            if not valid_cod(codigo, juegos):
                print("Codigo invalido o ya existente")

            elif not valid_text(titulo):
                print("Titulo invalido")

            elif not valid_text(plataforma):
                print("Plataforma invalida")

            elif not valid_text(genero):
                print("Género invalido")

            elif not valid_clasif(clasificacion):
                print("Clasificacion invalida")

            elif not calid_multi(multiplayer):
                print("Debe ingresar (si) o (no) en multiplayer")

            elif not valid_text(editor):
                print("Editor invalido")

            elif not valid_prec(precio):
                print("Precio invalido")

            elif not valid_stock(stock):
                print("Stock invalido")

            else:

                multiplayer_vf = multiplayer.strip().lower() == "si"

                if agreg_juego(
                        codigo,
                        titulo.strip(),
                        plataforma.strip(),
                        genero.strip(),
                        clasificacion.strip().upper(),
                        multiplayer_vf,
                        editor.strip(),
                        precio,
                        stock,
                        juegos,
                        inventario):

                    print("Juego agregado")

                else:
                    print("El codigo ya existe")

        except:
            print("Precio y stock deben ser numeros enteros")


    elif opc == 5:

        codigo = input("Ingrese el codigo del juego: ")

        if elimi_juego(codigo, juegos, inventario):
            print("Juego eliminado")
        else:
            print("El codigo no existe")


    elif opc == 6:
        print("Fin del programa.")
        break

puntuaciones = [5, 10, 20, 30, 30, 35, 40, 60, 100]
multiplicadores = [1, 2, 2, 3, 4, 4, 4, 7, 8]

def mayor_combinacion(cartas):
    if escalera_color(cartas):
        return 8
    elif poker(cartas):
        return 7
    elif full(cartas):
        return 6
    elif color(cartas):
        return 5
    elif escalera(cartas):
        return 4
    elif trio(cartas):
        return 3
    elif doble_pareja(cartas):
        return 2
    elif pareja(cartas):
        return 1
    else:
        return 0
def escalera_color(cartas):
    return False
def poker(cartas):
    return False
def full(cartas):
    return False
def color(cartas):
    return False
def escalera(cartas):
    return False
def trio(cartas):
    return False
def doble_pareja(cartas):
    return False
def pareja(cartas):
    return False
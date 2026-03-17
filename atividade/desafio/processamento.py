def validar_notas(notas):
    if type(notas) != list or len(notas) == 0:
        return False

    for nota in notas:
        if type(nota) != int and type(nota) != float:
            return False

    return True

def calcular_media(notas):
    return sum(notas) / len(notas)
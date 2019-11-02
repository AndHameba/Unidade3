#-*-coding:latin1-*-

def soma_lista(lista):
    """
    Soma listas de listas, recursivamente
    coloca o resultado como global

    """
    global soma

    for item in lista:
        if type(item) is list:
            soma_lista(item)
        else:
            soma += item

soma = 0
soma_lista([
    [1, 2, 5, 7, 9], [3, 4, [2, 2, 2]], [1, 1, 1]])

print soma
import random


def busqueda_lineal(lista, objetivo):
    match = False
    i = 0
    for elemento in lista:  # O(n)
        i += 1
        if elemento == objetivo:
            match = True
            break

    return match, i


def busqueda_binaria(lista, comienzo, final, objetivo, i=1):
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True, i
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, i + 1)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, i + 1)


if __name__ == '__main__':

    # Para búsqueda lineal
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    print(lista)

    encontrado, i = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Se usaron {i} iteraciones')

    encontrado, i = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Se usaron {i} iteraciones')

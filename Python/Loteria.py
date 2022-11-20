from random import randrange

def generarGanadores(cantGanadores,compartirPozo):
    listaGanadoras = [[] for i in range(0,cantGanadores)]
    if compartirPozo is True:
        listaUsada = []
    for i in range(0,cantGanadores):
        while len(listaGanadoras[i]) <=5:
            numeroSacado = randrange(0,99)
            if compartirPozo is True:
                if numeroSacado not in listaUsada and numeroSacado not in listaGanadoras[i]:
                    listaGanadoras[i].append(numeroSacado)
                    listaUsada.append(numeroSacado)
            else:
                if numeroSacado not in listaGanadoras[i]:
                    listaGanadoras[i].append(numeroSacado)
    return listaGanadoras

print("---- Sorteo ----")
cantidadListas = int(input("Cuantas listas ganadoras queres generar? - "))
preguntaPozo = input("Compartir pozo de numero entre listas? S/N - ")

match preguntaPozo:
    case "S":
        compartirPozo = True
        print(generarGanadores(cantidadListas,compartirPozo))
    case "N":
        compartirPozo = False
        print(generarGanadores(cantidadListas,compartirPozo))
    case _:
        print("Por favor escribir entre S / N")
input()



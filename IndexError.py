try:
    lista = [1, 2, 3]
    num = 3
    valor = lista[num]
except IndexError:
    print("A posiçao está fora da lista")
finally:
    print("Fim do programa")

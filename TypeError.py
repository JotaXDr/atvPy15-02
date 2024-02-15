try:
    resultado = "2" + 2
except TypeError as e:
    print("Erro de tipo: {}".format(e))
finally:
    print("finalizando")

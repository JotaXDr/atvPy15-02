try:
    resultado = 1 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero")
finally:
    print("Finalizando")

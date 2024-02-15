variavel = 'ola'
try:
    print(variavelIndefinida)
except NameError:
    print("Erro de nome, variavel nao encontrada")
finally:
    print('Finalizando...')

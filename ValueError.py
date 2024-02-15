try:
    num = int(input("Digite um número inteiro: "))
except ValueError:
    print("invalido")
finally:
    print("Fim do programa")

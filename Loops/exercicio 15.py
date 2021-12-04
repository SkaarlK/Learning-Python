import sys
valorTotal = 0;
while True:
    codigo = int(input("Insira o código do produto: "))
    if codigo != 0 and (codigo == 1 or codigo == 2 or codigo == 3 or codigo == 5 or codigo == 9):
        quantia = int(input("E a quantidade?: "))
        if codigo == 1:
            valor = 0.5
        elif codigo == 2:
            valor = 1
        elif codigo == 3:
            valor = 4
        elif codigo == 5:
            valor = 7
        elif codigo == 9:
            valor = 8
        valorTotal += valor * quantia
    elif codigo == 0:
        print("O preço total é: R$" + str(valorTotal))
        sys.exit(0)
    else:
        print("Código inválido.")



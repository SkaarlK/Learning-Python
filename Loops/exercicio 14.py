import sys
media = 0; soma = 0; quantia = 0;
while True:
    numeroDigitado = int(input("Digite um número inteiro: "))
    if numeroDigitado != 0:
        soma += numeroDigitado
        quantia += 1
    else:
        media = soma / quantia
        print("Você digitou um total de: " + str(quantia) + " números (mais o 0), sendo a soma deles: " + str(soma) + ", e sua média: " + str("%.2f" % media))
        sys.exit(0)
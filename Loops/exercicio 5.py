maximoImpar = int(input("Até que número gostaria de lista os múltiplos de 3?: "))
for x in range(maximoImpar):
    if x % 3 == 0:
        print(x)
        if x == 27:
            print("Acima estão os 10 primeiros múltiplos de 3.")
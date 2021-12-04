y = int(input("Qual número deseja obter as multiplicações?: "))
minimo = int(input("Desde que multiplicando deseja começar?: "))
maximo = int(input("Até qual multiplicando deseja ir?: "))
for x in range(maximo+1):
    if x >= minimo:
        print(str(x) + "x" + str(y) + " = " + str(x * y))
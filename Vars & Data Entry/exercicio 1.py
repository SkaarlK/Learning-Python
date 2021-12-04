import math
vars = [0,0];
print ('Insira 2 números para serem somados.')
for x in range(2):
    vars[x] = int(input())
    print("Insira o próximo número.")
print("Resultado:")
print(math.fsum(vars))
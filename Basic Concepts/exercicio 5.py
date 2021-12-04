import math
vars = [0,0,0];
print ('Insira 3 números para serem todos somados.')
for x in range(3):
    vars[x] = int(input())
    print('Insira o próximo número.')
print("Resultado:" + math.fsum(vars))
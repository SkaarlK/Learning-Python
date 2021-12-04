from decimal import Decimal 
n1 = int(input("Insira um número para verificar se é palíndromo: "))
copia = Decimal('%i' % n1)
nStr = str(copia)[::-1]
if int(nStr) == n1:
    print("Palíndromo.")
else:
    print("Não é.")


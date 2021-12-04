from decimal import Decimal
n = Decimal(float(input("Insira o Número que deseja saber a raiz: ")))
def raiz(x):
    r = x/Decimal('2')
    while True:
        oldR = r
        r = Decimal((((r * r) + x) / (Decimal('2') * r)))
        if (abs(r - oldR) < 0.0001):
            return r
resultado = raiz(n)
print("%.7f" % resultado)
from decimal import Decimal
ns = []
n1 = int(input("Insira um número para verificar os primos até ele: "))
def validaP3(n):
    soma = 0
    copia = str(n)
    tamanho = len(Decimal(n).as_tuple().digits)
    for i in range(tamanho):
        soma += int(copia[i])
    if soma % 3 == 0:
        return {'div3': True, 'number': n}
    else:
        return {'div3': False, 'number': n}
def validaP5(n):
    if n % 5 == 0:
        return {'div5': True, 'number': n}
    else:
        return {'div5': False, 'number': n}
def validarBasico():
    for i in range(n1):
        if i > 1 and (i == 2 or i == 3 or i == 5 or i == 7):
            ns.append(i)
def validarAv():
    for i in range(8, n1 + 1):
        divideP3 = validaP3(i)
        divideP5 = validaP5(i)
        if (i % 2 != 0 and divideP3['div3'] == False and divideP5['div5'] == False) or i == n1:
            ns.append(i)
validarBasico()
validarAv()
print(ns)
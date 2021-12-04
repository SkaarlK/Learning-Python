montanteAtual = 0; lucro = 0
depositoI = int(input("Insira o valor do depósito inicial: "))
juros = (int(input("Qual a taxa de juros? (ex 2.11%): ")) / 100) 
aporteMensal = int(input("Insira o valor do aporte mensal: "))
for x in range(120):
    if x == 1:
        montanteAtual = depositoI
        lucro += montanteAtual * juros
    if x > 1:
        montanteAtual += aporteMensal
        lucro += montanteAtual * juros
    print("No mês: " + str(x) + ", o total acumulado é de: " + str("%.2f" % montanteAtual) + ". E o lucro com juros: " + str("%.2f" % (lucro)))
    montanteAtual += montanteAtual * juros
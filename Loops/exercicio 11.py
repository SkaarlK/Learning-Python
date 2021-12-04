depositoI = int(input("Insira o valor do depósito inicial: "))
juros = int(input("Qual a taxa de juros? (ex 2.11%): "))
montanteAtual = depositoI
for x in range(25):
    print("No mês: " + str(x) + ", o total acumulado é de: " + str("%.2f" % montanteAtual) + ". E o lucro com juros: " + str("%.2f" % (montanteAtual - depositoI)))
    montanteAtual += montanteAtual * (juros / 100)
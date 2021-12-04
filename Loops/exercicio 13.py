jurosAplicados = 0; jurosPagos = 0; dividaAtual = 0; x = 0;
valorInicial = int(input("Qual o valor da divida inicial?: "))
juros = int(input("E os juros mensais?: ")) / 100
aporteMensal = int(input("E o aporte mensal?: "))
dividaAtual = valorInicial + (valorInicial * juros)
while dividaAtual >= aporteMensal:
    if x > 0:
        dividaAtual += dividaAtual * juros
        dividaAtual -= aporteMensal
        jurosAplicados += dividaAtual * juros
        x += 1
    else:
        jurosAplicados = dividaAtual * juros
        x += 1
    print("No mês: " + str(x) + ", a divida restante é de: " + str("%.2f" % dividaAtual) + ". E os juros totais até o momento: " + str("%.2f" % (jurosAplicados)))
print("O total pago foi de: R$" + str("%.2f" % (valorInicial + jurosAplicados + dividaAtual)) + ", Ao longo de: " + str(x) + " Meses.")
#5 (cinco) prestações Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
valor = int(input("Qual o valor da compra para parcelar em 5x? "))
prestacao = valor / 5
print("Valor final em 5x prestações mensais sem juros: %.2f" % prestacao)
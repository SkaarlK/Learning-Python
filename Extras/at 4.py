#nome de um vendedor, o seu salário fixo e o total de vendas no mês. Sabendo que este vendedor 
#ganha 15% de comissão sobre suas vendas efetuadas. 
vendedor = {'nome':str, 'salario':float, 'vendas':int}

vendedor['nome'] = str(input("Qual o nome do vendedor? "))
vendedor['salario'] = float(input("Qual o salario fixo dele? "))
vendedor['vendas'] = int(input("Quantas vendas efetuou este mês? "))

print(vendedor)
print("O adicional recebido por ele será de: R$" + str(vendedor['vendas'] * 0.15))
#Faça um algoritmo que calcule o valor da conta de luz de uma
#pessoa. Sabe-se que o cálculo da conta de luz segue a tabela abaixo:
preco = float; tarifa = {1: 0.60, 2: 0.48, 3: 1.29}

kwh = float(input("Insira quantos KW/h você consumiu: "))
tipo = float(input("Insira o tipo de cliente: \n1. residencia\n2. comercio\n3. industria"))

preco = kwh * tarifa[tipo]
print("\nA conta será de: R$" + str(preco))
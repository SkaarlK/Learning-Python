#A concessionária de veículos CARANGO está vendendo os seus veículos com
#desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser
#pago pelo cliente. O desconto deverá ser calculado sobre o valor do veículo de
#acordo com o combustível (álcool - 25%, gasolina - 21% ou diesel - 14%). Com valor
#do veículo zero encerra entrada de dados. Informe total de desconto e total pago
#pelos clientes.
desconto = {1: 0.25, 2: 0.21, 3: 0.14, 'descontado':0}; valorVeiculo = float; tipo = str; preco = 0
	
while True:
	valorVeiculo = float(input("Qual o valor do veículo: ")); 
	if valorVeiculo == 0:
		exit()
	tipo = int(input("\nQual o tipo de combustivel? \n1 Álcool\n2 Gasolina \n3 Diesel \n-> "))
	if tipo > 0 and tipo < 4:
		desconto["descontado"] = desconto[tipo] * valorVeiculo
		preco = valorVeiculo - desconto["descontado"]
		print("\nO desconto foi de: " + str(desconto["descontado"]))
		print("E o preço de pagamento final foi: " + str(preco))
	else:
		print("Inseriu os dados errado...")
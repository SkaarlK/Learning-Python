#Faça um algoritmo que receba o número do mês e mostre o mês correspondente.
#Valide mês inválido.

mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
num = int(input("Insira o número do mês... "))
if num > 0 and num < 13:
	print(mes[num])
else:
	print("Número não corresponde a nenhum mês.")
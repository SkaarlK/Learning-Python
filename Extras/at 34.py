#Elabore um algoritmo que, dada a idade de um nadador.
#Classifique-o em uma das seguintes categorias:
#Infantil A = 5 - 7 anos Infantil B = 8 - 10 anos juvenil A = 11- 13 anos juvenil B = 14 - 17 anos Sênior = 18 - 25 anos
#Apresentar mensagem “idade fora da faixa etária” quando for outro ano não
#contemplado.

idade = int(input("Insira a idade do nadador."))
if idade >= 5 and idade <= 7:
	print("Infantil A")
elif idade >= 8  and idade <= 10:
	print("Infantil B")
elif idade >= 11  and idade <= 13:
	print("Juvenil A")
elif idade >= 14  and idade <= 17:
	print("Juvenil B")
elif idade >= 18  and idade <= 25:
	print("Sênior")
else:
	print("Idade fora da faixa etária.")
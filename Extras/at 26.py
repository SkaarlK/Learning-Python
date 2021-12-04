#Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o
#usuário digite um número que não esteja neste intervalo, exibir mensagem: número
#inválido.
extenso = {1: 'Um', 2: 'Dois', 3: 'Tres', 4: 'Quatro', 5: 'Cinco'}
n = int(input("Insira um número."))
if (n < 1 or n > 5):
	print('Número inválido.')
else:
	print(extenso[n])

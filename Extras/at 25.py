#Faça um algoritmo que leia dois números e identifique se são iguais ou diferentes.
#Caso eles sejam iguais imprima uma mensagem dizendo que eles são iguais. Caso
#sejam diferentes, informe qual número é o maior, e uma mensagem que são
#diferentes.
n = [float,float]
for i in range(1,3):
	n[i-1] = float(input("\nInsira o %d número: " % i))
n.sort()
if (n[0] != n[1]):
	print("\nOs números informados são diferentes! \nO maior número é: %d" % n[1])
else:
	print("Os números são iguais.")
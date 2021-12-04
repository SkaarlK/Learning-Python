#Faça um algoritmo que receba dois números e exiba o resultado da sua soma.
n = [float,float,0]
for i in range(2):
	n[i] = float(input("Insira o N%s: " % str(i+1)))
	n[2] += n[i]
print("A soma é: " + str(n[2]))
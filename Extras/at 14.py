#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior
n = [float,float]
for i in range(len(n)):
	n[i] = float(input("Insira o N%s: " % str(i+1)))
n.sort()
print("%.1f é o maior numero." % n[1])
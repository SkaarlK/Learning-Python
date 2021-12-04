#Leia dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.
n = [float,float,0,{'mult':0, 'div':0, 'soma':0, 'sub':0}]
for i in range(2):
	n[i] = float(input("Insira o N%s: " % str(i+1)))
	n[3]['soma'] += n[i]
	if i > 0:
		n[3]['mult'] = n[0] * n[1]
		n[3]['div'] = n[0] / n[1]
		n[3]['sub'] = n[0] - n[1]
print(n[3])
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < len(notas):
	notas[x] = float(input("Nota %d: " % int(x + 1)))
	soma += notas[x]
	x += 1

print("Média: %.2f" % (soma/x))


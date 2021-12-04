#Atividade 15: O que acontece quando dois valores são iguais? Rastreie o programa 6.44, mas com 
#a lista L = [ 3, 3, 1, 5, 4 ]

#O Algoritmo interpreta essa situação como 3 > 3 = False, então as posições 
# com numeros iguais são mantidas lado a lado ao fim da execução, nem mesmo se invertem de index.


## FONT 6-44.py
L = [ 3, 3, 1, 5, 4 ]
fim = len(L)

while fim > 1:
	trocou = False
	x = 0
	while x < (fim-1):
		if L[x] > L[x+1]: 
			trocou = True
			temp = L[x]
			L[x] = L[x+1]
			L[x+1] = temp
		x += 1
	if not trocou:
		break
	fim -= 1
for e in L:
	print(e)
## FONT 6-44.py
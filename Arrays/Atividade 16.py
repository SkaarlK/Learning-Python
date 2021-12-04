#Atividade 16: Modifique o programa 6.44 para ordenar a lista em ordem decrescente. 
L = [ 1, 2, 3, 4, 5 ] 
# deve ser ordenada como 
# L = [ 5, 4, 3, 2, 1 ]


## Forma que eu faria
L.sort()
L.reverse()
print(L)


## Forma Modificando o 6-44.py
## FONT 6-44.py
L = [ 1, 2, 3, 4, 5 ] 
fim = len(L)

while fim > 1:
	trocou = False
	x = 0
	while x < (fim-1):
		if L[x] < L[x+1]: 
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
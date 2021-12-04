#Atividade 14: O que aconteceu quando a lista já está ordenada? Rastreie o programa 6.44, mas 
#com a lista L = [ 1, 2, 3, 4, 5 ].

# A validação para saber se o proximo index é menor que o anterior não é True
# Devido a isso o laço é ignorado e Trocou sempre será false, saindo do escopo do while 
# e retornando ao escopo global, printando a lista inalterada.



## FONT 6-44.py
L = [ 2, 1, 3, 4, 5 ]
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

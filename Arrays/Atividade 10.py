#Modifique o programa da atividade 09 de forma a pesquisar p e v em toda a lista e
#informando ao usuário a posição onde p e a posição onde v foram encontrados.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0

if p in L:
	pPos = L.index(p)
	print("P: %d foi encontrado no index %d" % (p,pPos))
else:
	print("%d não encontrado na lista: " % p + str(L))
if v in L:
	vPos = L.index(v)
	print("V: %d foi encontrado no index %d" % (v,vPos))
else:
	print("%d não encontrado na lista: " % p + str(L))

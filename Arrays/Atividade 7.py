#Atividade 07: Faça um programa que lê uma expressão com parênteses. Usando pilhas, verifique se
#os parênteses foram abertos e fechados na ordem correta. Exemplo: (()) ok; ()()(()()) ok; ()) erro.

lista = []; parenteses = []
Str = str(input("\nInsira os parenteses...: "))
for i in Str:
	if (i == "(" or i == ")"):
		parenteses.append(i)
for j in parenteses:
	if j == "(":
		lista.append(j)
	else:
		if len(lista) > 0:
			if lista[len(lista)-1] == "(":
				lista.pop()
			else:
				print("String não contém os parenteses fehcados da forma correta.")
				exit()
		else:
				print("String não contém os parenteses fehcados da forma correta.")
				exit()
print("Os parenteses foram fechados corretamente.")
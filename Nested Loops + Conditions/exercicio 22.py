#Escreva um programa que exiba uma lista de opções (menu): adição, subtração,
#divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída
#seja escolhida
n1 = 0; n2=0
while True:
    escolha = int(input("Digite: \n1 para Adição\n2 para Subtração\n3 para multiplicação\n4 para Divisão\n5 para Sair\n"))
    if escolha == 5:
        break
    else:
        n1 = float(input("Insira o N1: "))
    if escolha == 1:
        for i in range(11):
            print(str(i)+" + "+str(n1)+" = " + str(n1+i))
    elif escolha == 2:
        for i in range(11):
            print(str(n1)+" - "+str(i)+" = " + str(n1-i))
    elif escolha == 3:
        for i in range(11):
            print(str(n1)+" / "+str(i)+" = " + str(n1/i))
    elif escolha == 4:
        for i in range(11):
            print(str(i)+" * "+str(n1)+" = " + str(n1*i))
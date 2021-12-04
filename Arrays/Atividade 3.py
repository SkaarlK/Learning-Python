L = [2,4,6,7,27,30,30,72]
L2 = [2,6,7,9,11,72,30,30,30]
#L = []
#L2 = []
L3 = []
#for counter in range(int(input("quantos itens você deseja inserir na lista 1?: "))):
#    arg = int(input("Número "+str(counter + 1)+": "))
#    L.append(arg)

#for counter2 in range(int(input("quantos itens você deseja inserir na lista 2?: "))):
#    arg1 = int(input("Número "+str(counter2 + 1)+": "))
#    L2.append(arg1)

def valida(argJ):
    for counter in range(len(L2)):
        try:
            if (L3.index(argJ) != -1):
                return True
        except ValueError:
            if argJ == list:
                for j in range(len(argJ)):
                    L3.append(argJ[j])
            L3.append(argJ)
for i in range(len(L)):
    valida(L[i])
    if i <= len(L2):
        valida(L2[i])

print(L3)
    
        
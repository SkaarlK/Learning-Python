materia = [0,0,0]; soma = 0; media = 0
for x in range(len(materia)):
    materia[x] = float(input("Digite a nota da materia" + str(x + 1) + ": "))
    soma += materia[x]
media = soma / len(materia)
if media > 7:
    print("Aprovado")
    print("Média Final: " + str(round(media, 1)))
else:
    print("Reprovado.")
    print("Média Final: " + str(round(media, 1)))
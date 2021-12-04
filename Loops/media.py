n = [float,float,float,float]; soma = 0; md1 = 0; md2 = 0; pf = 0
print("Utilize apenas números, Ex: '6.75' '5' '8.2' caso contrário o programa será encerrado.")
for x in range(len(n)):
    n[x] = float(input("Digite a nota " + str(x + 1) + ": "))
    soma += n[x]
md1 = soma / len(n)
if md1 >= 7:
    print("Aprovado")
    print("Média Final: " + str(round(md1, 1)))
else:
    pf = float(input("Você não obteve a média apenas com as provas, informe a nota da Prova Final: "))
    md2 = (md1 + pf) / 2
    if md2 >= 5:
        print("Aprovado em prova final")
    else:
        print("Reprovado.")
print("Média Final: " + str(round(md2, 1)))
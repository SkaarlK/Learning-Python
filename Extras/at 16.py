#leia o nome e três notas e informar
#média, Aprovado (>= 7), Reprovado (<= 5) e Recuperação (5.1 a 6.9).

aluno = [float,float,float,str]; soma = 0; md1 = 0
aluno[3] = str(input("Qual o nome do aluno? "))
print("Utilize apenas números, Ex: '6.75' '5' '8.2' caso contrário o programa será encerrado.")
for i in range(3):
    aluno[i] = float(input("Digite a nota %d: " % (i+1)))
    soma += aluno[i]
md1 = soma / 3
print("O aluno %s esta: " % aluno[3])
if md1 >= 7:
    print("Aprovado")
elif md1 > 5:
    print("Recuperação")
else:
    print("Reprovado")
print("Média Final: %.1f" % md1)
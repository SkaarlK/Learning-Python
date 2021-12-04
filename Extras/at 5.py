#leia o nome e três provas. No final informar o nome a sua média (aritmética).
aluno = {'nome':str, 'notas': [float,float,float], 'media': 0}
str(input("Qual o nome do aluno? "))
for i in range(len(aluno['notas'])):
	aluno['notas'][i] = float(input("Insira a nota %s: " % str(i+1)))
	aluno['media'] += aluno['notas'][i]
aluno['media'] /= len(aluno['notas'])
print(aluno)
#Determinada escola faz o pagamento de seus professores por hora/aula. Faça um
#algoritmo que calcule e exiba o salário de um professor. Sabe-se que o valor da
#hora/aula segue a tabela abaixo:
#Professor Nível 1 R$12,00 por hora/aula
#Professor Nível 2 R$17,00 por hora/aula
#Professor Nível 3 R$25,00 por hora/aula

nivel = {1: 12, 2: 17, 3: 25}
prof = int(input("Qual o seu nível de professor: \n'1', '2' ou '3': "))
horas = int(input("Quantas horas deu aula: "))

print("Salario: R$%d" % (nivel[prof] * horas))
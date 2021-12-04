salario = int(input("Insira o salário: "))
if salario > 1250:
    salario += 0.10 * salario
elif salario <= 1250:
    salario += 0.15 * salario
print("R$" + str(salario))
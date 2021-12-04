valorCasa = int(input("Qual o valor da casa?: "))
salario = int(input("Qual o seu salário?: "))
tempo = int(input("Em quantos anos pretende pagar esse financiamento?: "))
if (valorCasa / (tempo * 12)) > (salario * 0.3):
    print("NEGADO.")
else:
    print("CONCEDIDO.")
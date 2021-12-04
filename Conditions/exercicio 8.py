import sys
vars = [0,0];
print ('Insira 2 números para serem operados.')
for x in range(2):
    vars[x] = int(input("N" + str(x+1) + ": "))
operacao = str(input("Qual operação deseja Realizar '+'   '-'   '/'   '*': "))
if operacao == "+":
    result = vars[0] + vars[1]
elif operacao == "-":
    result = vars[0] - vars[1]
elif operacao == "/":
    result = vars[0] / vars[1]
elif operacao == "*":
    result = vars[0] * vars[1]
else:
    print("Operação Inválida, preste atenção às possibilidades citadas.")
    sys.exit()
print("Resultado da operação: " + str(result))
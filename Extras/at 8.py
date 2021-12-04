#Ler cotação e converter Real em Dollar
cotacao = float(input("Qual a cotação atual do Dollar Americano (formato: 5.22)? "))
dollar = float(input("Quantos dollares deseja converter? "))
real = dollar / cotacao
print ("R$%.2f" % real)
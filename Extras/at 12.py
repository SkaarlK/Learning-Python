#O custo ao consumidor é o (custo de fábrica + impostos) + a percentagem do distribuidor
#Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. 
percentagemDistribuidor = 28 / 100
impostos = 45 / 100

custo = float(input("Qual o custo de fábrica do carro? "))
custo += (custo * impostos)
custo += (custo * percentagemDistribuidor)
print("O preço para consumidor final é de: R$%.2f" % custo)
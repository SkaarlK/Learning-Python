kWh = int(input("Qual foi o consumo em kWh: "))
print("'R' para Residências, 'I' para Indústrias e 'C' para Comércios")
tipo = str(input("Qual a sua instalação?: "))
if tipo == 'R' or tipo == 'r':
    if kWh <= 500:
        preco = kWh * 0.40
    elif kWh > 500:
        preco = kWh * 0.65
elif tipo == 'C' or tipo == 'c':
    if kWh <= 1000:
        preco = kWh * 0.55
    elif kWh > 1000:
        preco = kWh * 0.60
elif tipo == 'I' or tipo == 'i':
    if kWh <= 5000:
        preco = kWh * 0.55
    elif kWh > 5000:
        preco = kWh * 0.60
print("O preço estimado para o consumo de: " + str(kWh) + " kWh e instalação tipo: " + str(tipo) + ", é de: R$" + str("%.2f" % round(preco,2)))
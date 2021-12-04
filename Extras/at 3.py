#consumo médio de distância total percorrida e o total de combustível gasto.
n = [float,float,0,0]
n[0] = float(input("Insira a distância percorrida pelo automóvel: "))
n[1] = float(input("Insira o combustível gasto: "))

n[2] = n[0] / n[1]
n[3] = n[1] / n[0]
print("A eficiência do combustível foi de %.2f L/km rodado, ou " % n[2] + str(n[3]) + "km/L")
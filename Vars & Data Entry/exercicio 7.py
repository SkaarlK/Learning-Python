distancia = int(input("Por quantos KM você percorreu com o veículo?: "))
tempo = int(input("Por quantos DIAS você percorreu com o veículo?: "))
print("A taxa do aluguel será de: " + str((distancia * 0.15) + (tempo * 60)))
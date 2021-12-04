distancia = int(input("Digite a distância da viagem, em KM: "))
velocidade = int(input("Digite a velocidade média em Km/h: "))
tempo = distancia / velocidade
print ("O tempo para chegar ao destino é de: " + str(tempo) + " hora(s), convertendo para " + str(tempo * 60) + " minuto(s)")
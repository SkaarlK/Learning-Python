resultado = 0; vars = [0,0]
print ('Insira 2 números para serem divididos.')
for x in range(2):
    vars[x] = int(input("N" + str(x+1) + ": "))
n1 = vars[0]
n2 = vars[1]
while True:
    if vars[0] >= vars[1]:
        vars[0] -= vars[1]
        resultado += 1
    if not vars[0] >= vars[1]:
        break
print("A divisão de: " + str(n1) + " por " + str(n2) + " resulta em " + str(resultado))
print("O resto dessa divisão é: " + str(vars[0]))
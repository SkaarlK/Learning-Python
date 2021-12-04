vars = [0,0];
print ('Insira 2 números para serem multiplicados.')
for x in range(2):
    vars[x] = int(input("N" + str(x+1) + ": "))
stringTotal = str(vars[0]) + "x" + str(vars[1]) + " = "
for x in range(vars[0]):
    stringTotal += str(vars[1]) + " + "
stringTotal = stringTotal[:-3]
stringTotal += " = "
for x in range(vars[1]):
    stringTotal += str(vars[0]) + " + "
stringTotal = stringTotal[:-3]
print(stringTotal)
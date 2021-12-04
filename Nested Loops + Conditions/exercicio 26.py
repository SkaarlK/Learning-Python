n = [int,int]; resultado = 0;
for i in range(len(n)):
    n[i] = int(input("Insira o N%i: " % int(i+1)))
dsr = n[0]; dnd = n[1];
while dnd <= dsr:
    dsr -= dnd
    resultado += 1
print(str(n[0]) + " / " + str(n[1]) + " = " + str(resultado))
if dsr != 0:
    print(str(dsr) + " é o resto dessa operação.")
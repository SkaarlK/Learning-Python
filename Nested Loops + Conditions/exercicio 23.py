n = int(input("Insira um número para saber se é primo: "))

nope = 0
for i in range(n):
    if i > 1:
        if (n % i == 0):
            nope += 1

if n != 1 and n != 0 and nope == 0 :
    print("É primo")
    exit()
print("Não é primo.")
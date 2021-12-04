#Ler 80 números e informar quantos estão no intervalo entre 10 (inclusive) e 150 (inclusive).
nums = []
quantia = str(input("Quantos números você deseja inserir (deixe em branco para 80)? "))
def addNumber():
		newNumber = int(input("Insira o Número: "))
		if newNumber >= 10 and newNumber <= 150:
			nums.append(newNumber)
if quantia:
	for i in range(int(quantia)):
		addNumber()
else:
	for i in range(80):
		addNumber()
print("No intervalo, houveram %d números. Sendo eles: " % len(nums) + str(nums))
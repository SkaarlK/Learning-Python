#Escrever um algoritmo que leia três valores inteiros distintos e os escreva em ordem
#crescente.
nums = [float,float,float]
for i in range(len(nums)):
	nums[i] = float(input('Insira o %d número: ' % int(i+1)))
nums.sort()
print(nums)

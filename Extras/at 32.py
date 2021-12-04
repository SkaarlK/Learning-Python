#Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os
#lados de um triângulo. Se forem, informar qual o tipo de triângulo que eles formam:
#equilátero, isóscele ou escaleno.
lado = [float,float,float]

for i in range(len(lado)):
	lado[i] = float(input("Insira o Lado %d: " % i))
a = lado[0]; b = lado[1]; c = lado[2]
if (abs(b - c) < a and a < abs(b + c)) and (abs(a - c) < b and b < abs(a + c)) and (abs(a - b) < c and c < abs(a + b)):
	def classificaTri():
		if (a == b and b == c and c == a):
			return ("Triangulo equilátero")
		elif ((a != b,c and b == c) and (b != c,a and c == a) and (c != b,a and b == a)):
			return("Triangulo Isóceles")
		else:
			return("Triangulo escaleno")
	print(classificaTri())

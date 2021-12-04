#Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos.
#Mostre como resultado se houve lucro, prejuízo ou empate para cada produto.
#Informe media de preço de custo e do preço de venda.
produtos = []; mediaCusto = 0; mediaVenda = 0
class Produto:
	produto = str
	custo = float
	venda = float
	def __init__(self, produto, custo, venda):
		self.produto = produto
		self.custo = custo
		self.venda = venda
	def lucro(self):
		return self.venda - self.custo
	
for i in range(1, 3):
	produto = Produto(str(input('\nInsira o produto: ')), float(input('Custo: ')), float(input('Venda: ')))
	produtos.append(produto)
	print("\nFaturou: " + str(produto.lucro()))
	mediaCusto += produtos[i-1].custo
	mediaVenda += produtos[i-1].venda

mediaCusto /= len(produtos)
mediaVenda /= len(produtos)

print("\nAs médias de Custo/Venda são: " + str(mediaCusto) + " / " + str(mediaVenda))
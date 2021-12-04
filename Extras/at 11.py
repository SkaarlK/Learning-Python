#preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
preco = float(input("Preço de custo: "))
acrescimo = float(input("Qual o acrescimo (formato: 50%): "))
preco += preco * (acrescimo / 100)
print("O preço final: R$%.2f" % preco)
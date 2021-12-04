tempo = int(input("Há quantos anos aproximadamente você fuma cigarros?: "))
quantidade = int(input("E qual o valor médio de cigarros por dia?: "))
reducao = ((quantidade * 10) * (tempo * 365)) / 1440
print("A média de redução de vida está por volta de: " + ("%.1f" % reducao) + " dias de vida a menos")
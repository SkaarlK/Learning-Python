pontos = 0; questao = 1
while questao <= 3:
    resposta = input("A resposta da questão %d: " % questao)
    if questao == 1 and resposta.lower() == "b":
        pontos = pontos + 1
    if questao == 2 and resposta.lower() == "a":
        pontos = pontos + 1
    if questao == 3 and resposta.lower() == "d":
        pontos = pontos + 1
    questao += 1

print("O aluno fez %d ponto(s)" % pontos)

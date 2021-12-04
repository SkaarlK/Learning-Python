valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor
while True:
    if apagar <= 0.09:
        if apagar > 0.009:
            apagar = round(apagar,2)
        else:
            apagar = round(apagar,3)
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1 and cedulas != 0:
            print("%d cédula(s) de R$%d" % (cedulas, atual))
        elif cedulas != 0:
            print("%d moeda(s) de %d centavos" % (cedulas, atual * 100))
        if apagar < 0.01 and apagar != 0:
            print("1 moeda de %.3f centavos" % (apagar))
            break
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0
        
        
        
        

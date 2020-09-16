variavel=0
texto=""
idade=(int(input("Insira a sua idade: ")))
peso=(float(input("Insira o seu peso: ")))
tempo=(float(input("Insira quantas horas de sono tiveste na ultima noite: ")))

if idade>16 and idade<69:
    variavel+=1
else:
    texto="idade "+texto

if peso>50:
    variavel+=1
else:
    texto="peso "+texto

if tempo>6:
    variavel+=1
else:
    texto="sono "+texto

if variavel==3:
    print("Pode doar sangue")
else:
    print("Não pode doar sangue pois não atingiu o experado nas categorias de:",texto)
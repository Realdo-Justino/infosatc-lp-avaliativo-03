nome=[]
cpf=[]
senha=[]
apto=[]
usuario=0
for x in range(5):
    texto=""
    alternativa=""
    variavel=0
    print("")
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
        alternativa=(input("Deseja se cadastrar?(s/n): "))
        if(alternativa=="s"):
            usuario=usuario+1
            variavel=(input("Insira seu nome: "))
            nome.append(variavel)
            variavel=(float(input("Insira seu cpf: ")))
            cpf.append(variavel)
            variavel=(input("Insira sua senha: "))
            senha.append(variavel)
            variavel=(input("Está apto a doar? "))
            apto.append(variavel)
        else:
            pass
    else:
        print("Não pode doar sangue pois não atingiu o experado nas categorias de:",texto)

for x in range(usuario):
    print("")
    print("O nome do usuario ",x," é ",nome[x])
    print("O cpf do usuario ",x," é ",cpf[x])
    print("A senha do usuario ",x," é ",senha[x])
    print("O usuario ",x," esta apto? ",apto[x])

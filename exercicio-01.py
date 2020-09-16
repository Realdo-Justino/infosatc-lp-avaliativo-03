numero=int(input("Insira um numero de 1 a 12: "))-1
mes=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
variavel=0

for x in range(1,12):
    if x==numero:
        print("O mes correspondente é: ",mes[numero])
        variavel=1
if variavel==0:
    print("Valor fora de alcançe")
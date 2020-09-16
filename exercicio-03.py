mulheres=0
homens=0
idadeTotalF=0
idadeTotalM=0
for x in range(1):
    sexo=(input("Insira o seu sexo (f/m): "))
    if sexo=="m":
         mulheres=mulheres+1
         idadeTotalF=idadeTotalF+(int(input("Insira sua idade: ")))
    else:
        homens+=1
        idadeTotalM=idadeTotalM+(int(input("Insira sua idade: ")))

print("")
print("A media da idade das mulheres é",idadeTotalF/mulheres)
print("A media da idade dos homens é",idadeTotalM/homens)
print("A media da idade é",(idadeTotalF+idadeTotalM)/(mulheres+homens))
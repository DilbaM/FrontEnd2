alturas = []
generos = []
for i in range(15):
    altura = float(input(f"Digite a altura do usuário {i+1}: "))
    genero = input("Qual o seu genero? Digite M(MASCULINO) e F(FEMININO)").upper()
    alturas.append(altura)
    generos.append(genero)

menor_altura = min(alturas)
maior_altura = max(alturas)
total_homens = generos.count("M")
total_mulheres = generos.count("F")
soma_altura_homens = 0

for i in range(len(generos)):
    if generos[i] == "M":
        soma_altura_homens += alturas[i]
if total_homens ==0:
    total_homens= 0
else:
    media_altura_homens = soma_altura_homens / total_homens

print(f"A menor altura é: {menor_altura} metros e a maior altura é {maior_altura}")
print(f"Total de mulheres: {total_mulheres}")
if total_homens >0:
    print(f"Média de altura dos homens: {media_altura_homens:.2f} metros")

#prof1244@iesp.edu.br
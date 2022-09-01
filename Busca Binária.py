vetor = []

for i in range(0,10):
    vetor.append(int(input("elemento vetor:")))

vetor.sort()
elemento = int(input("elemento buscado:"))
inicio = 0
fim = len(vetor)-1
achou = False

while ((inicio <= fim) and (not achou)):
    meio = (inicio + fim)//2
    if elemento == vetor[meio]:
        position = meio
        achou = True
    elif elemento < vetor[meio]:
        fim += meio
    else:
        inicio += meio
if achou:
    print ("Encontrado! Posição:", position)
else:
    print("Não foi encontrado")

vetor = []
n = int(input("Número:"))

while n >= 0:
    vetor.append(n)
    n = int(input("Número:"))

for i in range(0,len(vetor)-1):
    for j in range(i+1,len(vetor)):
        if vetor[i] > vetor[j]:
            auxiliar = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = auxiliar
print ("Vetor ordenado:", vetor)

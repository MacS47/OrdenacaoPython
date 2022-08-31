import random

# vetor = [9,8,7,6,5,4,3,2,155,689,689,6,7,10,11,-55,-86]

vetor = []

for i in range(0,20000):
    vetor.append(random.randint(-50000000,50000000))

print(vetor)

for x in range(len(vetor)):
    k = 0
    for i in vetor:
        if(k < (len(vetor)-1)):
            if(i > vetor[k+1]):
                auxiliar = vetor[k+1]
                vetor[k+1] = vetor[k]
                vetor[k] = auxiliar
        k += 1
    
print(vetor)

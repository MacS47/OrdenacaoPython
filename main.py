import random

# Função resoponsável por criar um lista (array|vetor), que
# será populado com valores aleatórios. Os parâmetros 
# que devem ser informados são: o tamanho da lista,
# valor incia e valor final, lembrando que todos devem ser 
# inteiros.
def criar_lista(tamanho, val_inicial, val_final):
    
    vetor = []

    for i in range(0,tamanho):
        vetor.append(random.randint(val_inicial,val_final))
    
    return vetor

# Essa função realiza a ordenação do tipo Bubble Sort.
# Em resumo, o algoritmo realiza uma verificação:
# Se o valor do vetor armazenado no indíce atual for 
# maior do que do próximo indíce, estes serão trocados.
# Considerando que isso é feito com todos os itens desse vetor
def bubble(vetor):
    
    for x in range(len(vetor)):
        k = 0
        for i in vetor:
            if(k < (len(vetor)-1)):
                if(i > vetor[k+1]):
                    auxiliar = vetor[k+1]
                    vetor[k+1] = vetor[k]
                    vetor[k] = auxiliar
            k += 1
    
    return vetor

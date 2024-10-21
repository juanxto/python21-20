lista = [4, 6, 7, 6, 2, 6, 9, 10, 20, 20, 20]

#len - retorna o tamanho da lista
tamanho = len(lista)
print(tamanho)
print(len(lista))

#append - insere um item no final da lista
lista.append(20)
print(lista)

#max - retorna o maior item da lista
print(max(lista))

#min - retorna o menor item da lista
print(min(lista))

#com strings ele considera a ordem alfabética
nomes = ['marcelo', 'paulo', 'ana', 'joao']
print(max(nomes))
print(min(nomes))

#min e max não podem ser usadas quando tem strings e numeros em uma lista

#insert - insere um item em um indice
indice = int(input('Indice: '))
n = int(input('Numero: '))
lista.insert(indice, n)
print(lista)

#pop() - remove o ultimo item da lista
lista.pop()
print(lista)

#pop(indice) - remove o item de um indice
lista.pop(2)
print(lista)

#remove - remove a primeira ocorrencia de um item da lista
lista.remove(20)
print(lista)

#remover todas as ocorrencias de um item da lista
while 20 in lista:
    lista.remove(20)
print(lista)

#count - retorna a quantidade de vezes que um item aparece na lista
lista = [4, 6, 7, 8, 3, 4, 8, 10]
print(lista.count(4))

#index - retorna o indice de um item
print(lista.index(8))

#sort - ordena uma lista em ordem crescente
lista = [4, 7, 10, 234, 4, 6]
lista.sort()
print(lista)

#sort(reverse=True) - ordena uma lista em ordem decrescente
lista.sort(reverse=True)
print(lista)

#concatenação de lista
lista1 = [3, 6, 7]
lista2 = [60, 34, 654, 10, 3]
lista3 = lista1 + lista2
print(lista3)
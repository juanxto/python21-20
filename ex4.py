lista = []

while True:
    print('Digite 0 quando quiser terminar a lista')
    n = int(input('Adicione um número a lista: '))
    if n == 0:
        break
    lista.append(n)
lista1 = lista[::-1]
if lista1 == lista:
    print('Esta lista é um palíndromo')
else:
    print('Esta lista não é um palíndromo')
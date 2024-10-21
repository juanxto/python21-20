lista = []

while True:
    print('Digite 0 quando quiser terminar a lista')
    n = int(input('Adicione um número a lista: '))
    if n == 0:
        break
    lista.append(n)

listapar = []
listaimpar = []

for num in lista:
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
print(f'Lista de números pares inseridos: {listapar}')
print(f'Lista de números impares inseridos: {listaimpar}')

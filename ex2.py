lista = []

while True:
    print('Digite 0 quando quiser terminar a lista')
    n = int(input('Adicione um número a lista: '))
    if n == 0:
        break
    lista.append(n)

listaprimo = []

for num in lista:
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        listaprimo.append(num)
print(listaprimo)
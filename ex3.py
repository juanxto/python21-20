lista = []

while True:
    print('Digite 0 quando quiser terminar a lista')
    n = int(input('Adicione um número a lista: '))
    if n == 0:
        break
    lista.append(n)

n = int(input('Digite um numero: '))
print(f'A quantidade de vezes que {n} foram {lista.count(n)} vezes.')
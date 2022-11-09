
# STRING


nome = 'YANA DISCONZI'
nome1 = nome[0:4]
nome2 = nome[4:13]

print(nome1)
print(nome2)


'Y' in nome1

# LISTAS

lista = [1, 4, 6, 'Yana', 13, 14]
lista2 = [10, 20, 25, 34, 13, 14]

print(lista)
lista.append('Disconzi')
print(lista)
lista.append(6)
print(lista)

# Qual posição na lista

lista.index(13)

# Conta ocorrencias

lista.count(6)

# remove valor da lista

lista.remove('Yana')
print(lista)


# inverte a ordem da lista

lista.reverse()
print(lista)


# Ordena lista2

lista2.sort()
print(lista2)


# DICIONARIOS

telefones = {'Yana': 6182107469, 'Clara': 981316151, 'Roberta': 6198307100}
telefones

# Add a lista

telefones['Rita'] = 959595959
telefones


# Dell a lista

del telefones['Roberta']
telefones


# TUPLAS

tuplas = ('Yana', 'Python', 'udemy')
tuplas

tuplas[2]
tuplas[0:2]


len(tuplas)

tuplas+tuplas
tuplas*5

# transformar lista em tulpa

lista3 = tuple(lista)
lista3


# CONDIÇÕES

numero = 10

if (numero == 1):
    print('numero é igual a 1')
else:
    print('numero NÃO é igual a 1')


# LOOPS

for x in range(0, 5):
    print('Valor de x é:', x)


name = 'Yana'

for letra in name:
    print(letra)


for valor in lista:
    print(valor)


# WHILE LOOP

numero = 13
while (numero > 0):
    print(numero)
    numero = numero-1


# PASS BREAKE CONTINUE

numero = 30
while True:
    numero = numero-1
    print(numero)
    if (numero == 20):
        continue
    if (numero == 13):
        break


numero = 15
while True:
    numero = numero-1
    if (numero == 10):
                 continue
    print(numero)
    if (numero == 3):
        break

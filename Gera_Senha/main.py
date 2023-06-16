#Gerador de senha

import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
char_especial = chr(33)

lista_senha = []


for i in range(6):
    numeros = random.randrange(9)
    lista_senha.append(numeros)
random.shuffle(lista_senha)

print(lista_senha)
# BIBLIOTECAS EM PYTHON 

import random

nomes = [ ]
while True:
    nomes.append(input('Digite o nome: '))
    sair = input('Você deseja sair? [s] sim')
    if sair.lower() == 's':
        break
print(nomes)


   

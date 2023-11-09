import random 

nomes = [ ]
while True:
    nomes.append(input('Digite o nome: '))
    sair = input('Você deseja sortear os nomes? [s] sim')
    
    if sair.lower() == 's':
        ordem_Aleatoria = random.shuffle(nomes)
        print(ordem_Aleatoria)
        break

print('Vamos jogar um jogo de adivinhação. Tente adivinhar o número que estou pensando entre 1 e 10.')

import random 
numero_secreto = random.randint(1, 10)
tentativa = None

while tentativa != numero_secreto:
    tentativa = int(input('Digite o seu palpite: '))
    if tentativa < numero_secreto:
        print('Mais alto!')
    elif tentativa > numero_secreto:
        print('Mais baixo!')
    
print('Parabéns! Você adivinhou o número.')

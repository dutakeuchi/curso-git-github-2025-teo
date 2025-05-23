# programa para sortear um número entre 1 e 15. 
# o usuário deverá acertar o número escolhido em até 3 chances
# para cada erro, o programa irá informar se o número é
# maior ou menor
# %%
import random
# %%
n_sorteio = random.randint(1,15)
print(n_sorteio)
# %%
contador = 0
valid = False
while contador < 3:
    while valid == False:
        n_usuario = input('Digite um valor entre 1 e 15')
        try:
            n_usuario = int(n_usuario)
            if 1 <= n_usuario <= 15:
                valid = True
            else:
                print('Digite um valor entre 1 e 15')
        except:
            print('Digite um valor válido')
    valid = False        

    if n_usuario == n_sorteio:
        print('Parabéns, você acertou')
        break
    else:
        contador +=1
        if n_usuario > n_sorteio:
            print(f'o número sorteado é menor do que {n_usuario}')
        else:
            print(f'o número sorteado é maior do que {n_usuario}')
if contador == 3:
    print('Você não acertou o número sorteado')


# %%

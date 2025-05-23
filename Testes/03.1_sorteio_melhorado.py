# %%
import random

# %%
def get_input():
    while True:
        try:
            n_usuario = int(input('Digite um número entre 1 e 15'))
        except ValueError as err:
            print('Valor inválido')
            continue
        if 1 <= n_usuario <= 15:
            return n_usuario
        else:
            print('Digite um valor entre 1 e 15')

def check_number(sorteio, usuario):
    if n_sorteio == n_usuario:
        print(f'Parabéns, você ganhou! O número sorteado era {n_sorteio}')
        return True
    elif n_sorteio > n_usuario:
        print(f'o número sorteado é maior do que {n_usuario}.')
        return False
    else:
        print(f'o número sorteado é menor do que {n_usuario}.')
        return False

n_sorteio = random.randint(1,15)

for i in range(3):

    n_usuario = get_input()
    
    if check_number(n_sorteio, n_usuario):
        break

else:
    print(f'Você não acertou o número sorteado, que era {n_sorteio}')

# %%

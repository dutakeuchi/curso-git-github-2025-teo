# %%
a = 1
b = 5
# %%
print(a)
print(b)
# %%
a, b = b, a
print(a)
print(b)
# %%
dados = {'nome':'Joao','sobrenome':'Carvalho','nota':'10',
         'profissão':'advogado'}
for i, j in dados.items():
    print(i,j)
 # %%
dados.items()
# %%
for i in dados:
    print(i)
# %%
dados = {'nome':'Joao','sobrenome':'Carvalho'}
for i, j in dados.items():
    print(i,j)
# %%
dados.keys()
# %%
dados.values()
# %%
a, b, c, *_ = 1,5,6,8,546,456,4156
print(_)
# %%
def soma(*args):
    total = sum(args)
    return total

soma(1,5,6,8)
# %%

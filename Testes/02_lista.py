# %%
nome_arquivo = "02_lista.csv"

with open(nome_arquivo) as open_file:
    lista = open_file.readlines()

print(lista)


# %%
dicionario = {}
ch = lista[0].strip('\n').split(';')
for i in ch:
    dicionario[i] =[]

dicionario   
    

# %%
for i in range(1,len(lista)):
    valores = lista[i].strip('\n').split(';')
    for n in range(len(valores)):
        dicionario[ch[n]].append(valores[n])
dicionario




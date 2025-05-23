# %%
import requests
import json
from tqdm import tqdm
import pandas as pd

# %%
ceps = ['01519000','03432030','01311902',
        '13476863','53420160','09656000',
        '21870370','14400760','21645522'
        ]
url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

# %%
with open('04_ceps.json', 'w', encoding = 'utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
# %%
dataset = pd.DataFrame(dados)
dataset.to_csv('04_ceps.csv', sep=';', encoding='utf-8', index=False)
dataset
# %%

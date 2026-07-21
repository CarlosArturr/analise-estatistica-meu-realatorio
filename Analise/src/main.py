import matplotlib
matplotlib.use("TkAgg")

import seaborn as sns

import data as dt

sns.set_theme()

dados = dt.extract()

#informações gerais
print("="*60)
print("ESTRUTURA DOS DADOS")
print("="*60)

print(f"Linhas: {dados.shape[0]}")
print(f"Colunas: {dados.shape[1]}\n")

print(dados.info())

print("\nPrimeiras linhas:")
print(dados.head())

print("\nDicionário de Dados")
print(dt.dicionarioDados())

print("\nQualidade dos Dados")
print(dt.qualidadeDados(dados))



print("\nDados faltantes")
print(dt.ausenteDados(dados))

descritivas = (
    dados.drop(columns="id")
         .select_dtypes(include="number")
         .describe()
         .T
)

descritivas = descritivas.rename(columns={
    "count": "n",
    "mean": "media",
    "std": "dp",
    "min": "minimo",
    "25%": "q1",
    "50%": "mediana",
    "75%": "q3",
    "max": "maximo"
})

print("\nDescritivas")
print(descritivas.round(2))

# Transforma para formato longo (equivalente ao pivot_longer)
dados_longos = dt.dadosLongos(dados)

print(dados_longos.head())


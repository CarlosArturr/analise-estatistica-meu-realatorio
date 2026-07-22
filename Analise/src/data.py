import pandas as pd
from pathlib import Path

def extract():
    # Caminho do arquivo relativo ao próprio script
    arquivo = Path(__file__).resolve().parent.parent / "dados" / "04_Carseats.csv"

    # Lê os dados
    dados = pd.read_csv(arquivo)

    # Identificador das observações
    dados["id"] = range(1, len(dados) + 1)

    # Variáveis categóricas
    categorias = ["ShelveLoc", "Urban", "US"]
    dados[categorias] = dados[categorias].astype("category")

    return dados

def colunas():

    colunas = [
        "Sales",
        "CompPrice",
        "Income",
        "Advertising",
        "Population",
        "Price",
        "Age",
        "Education",
        "ShelveLoc"
    ]

    return colunas

def dicionarioDados():
    dicionario = pd.DataFrame({
    "Variável": [
        "Sales",
        "CompPrice",
        "Income",
        "Advertising",
        "Population",
        "Price",
        "ShelveLoc",
        "Age",
        "Education",
        "Urban",
        "US",
        "id"
    ],
    "Tipo": [
        "Numérica",
        "Numérica",
        "Numérica",
        "Numérica",
        "Numérica",
        "Numérica",
        "Categórica",
        "Numérica",
        "Numérica",
        "Categórica",
        "Categórica",
        "Inteira"
    ],
    "Papel": [
        "Resposta",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Preditor",
        "Identificador"
    ],
    "Descrição": [
        "Vendas unitárias (milhares)",
        "Preço do concorrente",
        "Renda local (milhares de dólares)",
        "Investimento em propaganda",
        "População (milhares)",
        "Preço da empresa",
        "Qualidade da prateleira",
        "Idade média",
        "Escolaridade média",
        "Loja urbana",
        "Loja nos EUA",
        "Identificador da observação"
    ]
})
    return dicionario

def qualidadeDados(dados): 
    qualidade = pd.DataFrame({
    "Observações": [len(dados)],
    "Variáveis": [dados.shape[1]],
    "Duplicatas": [dados.drop(columns="id").duplicated().sum()],
    "Observações com NA": [dados.isna().any(axis=1).sum()],
    "Valores ausentes": [dados.isna().sum().sum()],
    "ShelveLoc diferentes": [dados["ShelveLoc"].nunique()],
    "Urban diferentes": [dados["Urban"].nunique()],
    "US diferentes": [dados["US"].nunique()]
})
    return qualidade

def ausenteDados(dados):
    ausentes = pd.DataFrame({
    "Valores ausentes": dados.isna().sum(),
    "% ausentes": (100 * dados.isna().mean()).round(2)
})
    return ausentes

def variaveisNumericas():
    numericas = [
    "Sales",
    "CompPrice",
    "Income",
    "Advertising",
    "Population",
    "Price",
    "Age",
    "Education"
]
    return numericas

def dadosLongos(dados):
    dados_longos = dados.melt(
    id_vars="Sales",
    value_vars=variaveisNumericas(),
    var_name="Variavel",
    value_name="Valor"
)
    return dados_longos

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

import data as dt

PASTA_GRAFICOS = Path("../graficos")
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

PASTA_RESULTADOS = Path("../resultados")
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

dados = dt.extract()

#Relacionando sales as variaveis qualitativas

plt.figure(figsize=(6, 5))

cores = {
    "Bad": "#cb3028",      # vermelho
    "Medium": "#f7cd5c",   # amarelo
    "Good": "#1d874b"      # verde
}


sns.boxplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    order=["Bad", "Medium", "Good"],
    palette=cores
)

sns.stripplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    order=["Bad", "Medium", "Good"],
    color="black",
    alpha=0.4,
    jitter=0.2
)

plt.title("Distribuição das vendas por qualidade da prateleira")
plt.xlabel("Qualidade da Prateleira (ShelveLoc)")
plt.ylabel("Vendas (Sales)")

plt.tight_layout()
plt.savefig(
    PASTA_GRAFICOS / "sales_shelveloc.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(6,5))

cores = {
    "No": "#cb3028",      # vermelho
    "Yes": "#1d874b"      # verde
}

sns.boxplot(
    data=dados,
    x="Urban",
    y="Sales",
    hue="Urban",
    palette=cores,
    dodge=False,
    legend=False
)

sns.stripplot(
    data=dados,
    x="Urban",
    y="Sales",
    color="black",
    alpha=0.4,
    jitter=0.2
)

plt.title("Sales por localização urbana")

plt.savefig(
    PASTA_GRAFICOS / "sales_urban.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(6,5))

cores = {
    "No": "#cb3028",      # vermelho
    "Yes": "#1d874b"      # verde
}

sns.boxplot(
    data=dados,
    x="US",
    y="Sales",
    hue="US",
    palette=cores,
    dodge=False,
    legend=False
)

sns.stripplot(
    data=dados,
    x="US",
    y="Sales",
    order= ["No", "Yes"],
    color="black",
    alpha=0.4,
    jitter=0.2
)

plt.title("Sales por país")

plt.savefig(
    PASTA_GRAFICOS / "sales_us.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

#Metricas numericas

plt.figure(figsize=(6,5))

g = sns.pairplot(
    dados[dt.colunas()],
    corner=True,
    diag_kind="kde"
)

g.figure.suptitle(
    "Relações entre as variáveis numéricas",
    y=1.02
)

g.figure.savefig(
    PASTA_GRAFICOS / "pairplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(g.figure)

plt.figure(figsize=(6,5))

sns.boxplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    order=["Bad","Medium","Good"],
    showmeans=True,
    meanprops={
        "marker":"D",
        "markerfacecolor":"red",
        "markeredgecolor":"black"
    }
)

plt.figure(figsize=(6,5))

sns.pointplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    order=["Bad","Medium","Good"],
    errorbar=("ci",95)
)

plt.title("Média de Sales por qualidade da prateleira")

plt.savefig(
    PASTA_GRAFICOS / "media_sales_shelveloc.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

numericas = dados.select_dtypes(include="number").drop(columns="id")

matriz_cor = numericas.corr()

print(matriz_cor.round(3))

matriz_cor.round(3).to_csv(
    PASTA_RESULTADOS / "matriz_correlacao.csv",
    index=True
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    matriz_cor,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5
)

plt.title("Matriz de Correlação")

plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "matriz_correlacao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

dados_corr = dt.dados_convertidos_int()

numericas = dados_corr.select_dtypes(include="number").drop(columns="id")

matriz_cor = numericas.corr(method="spearman")

print(matriz_cor.round(3))

matriz_cor.round(3).to_csv(
    PASTA_RESULTADOS / "matriz_correlacao.csv"
)

plt.figure(figsize=(12, 10))

sns.heatmap(
    matriz_cor,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    square=True
)

plt.title("Matriz de Correlação (incluindo variáveis categóricas codificadas)")

plt.tight_layout()

plt.savefig(
    PASTA_GRAFICOS / "matriz_correlacao_total.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
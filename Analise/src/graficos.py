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

ordem = ["Bad", "Medium", "Good"]
cores = {
    "Bad": "#d73027",      # vermelho
    "Medium": "#fee08b",   # amarelo
    "Good": "#1a9850"      # verde
}


sns.boxplot(
    data=dados,
    x="Urban",
    y="Sales",
    palette=cores,
    legend=False
)

sns.stripplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    order=ordem,
    color="black",
    alpha=0.4,
    jitter=True
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
    "No": "#d73027",      # vermelho
    "Yes": "#1a9850"      # verde
}

sns.boxplot(
    data=dados,
    x="Urban",
    y="Sales",
    palette=cores
)

sns.stripplot(
    data=dados,
    x="Urban",
    y="Sales",
    color="black",
    alpha=0.4
)

plt.title("Sales por localização urbana")

plt.savefig(
    PASTA_GRAFICOS / "sales_urban.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(6,5))

sns.boxplot(
    data=dados,
    x="US",
    y="Sales"
)

sns.stripplot(
    data=dados,
    x="US",
    y="Sales",
    color="black",
    alpha=0.4
)

plt.title("Sales por país")

plt.savefig(
    PASTA_GRAFICOS / "sales_us.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
"""
#Metricas numericas

dados = dt.extract()
numericas = dt.variaveisNumericas()
dados_longos = dt.dadosLongos(dados)
g = sns.catplot(
    data=dados_longos,
    x="Sales",
    y="Valor",
    col="Variavel",
    kind="box",
    col_wrap=2,
    sharey=False,
    height=4,
    color="lightgray"
)

for ax, variavel in zip(g.axes.flat, numericas):

    sns.stripplot(
        data=dados_longos[dados_longos["Variavel"] == variavel],
        x="Sales",
        y="Valor",
        color="black",
        alpha=0.5,
        size=3,
        jitter=0.2,
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Valor")

colunas = dt.colunas()

g = sns.pairplot(
    dados[colunas],
    hue="Sales",
    diag_kind="kde",
    corner=False,
    plot_kws={"alpha": 0.6, "s": 25},
    diag_kws={"fill": True}
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


# Seleciona apenas as variáveis numéricas
numericas = dados.select_dtypes(include="number").drop(columns="id")

# Matriz de correlação de Pearson
matriz_cor = numericas.corr()

# Arredonda para 3 casas decimais
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
"""
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

import data as dt

PASTA_GRAFICOS = Path("../graficos")
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

PASTA_RESULTADOS = Path("../resultados")
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

dados = dt.extract()
numericas = dt.variaveisNumericas()
dados_longos = dt.dadosLongos(dados)
g = sns.catplot(
    data=dados_longos,
    x="ShelveLoc",
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
        x="ShelveLoc",
        y="Valor",
        color="black",
        alpha=0.5,
        size=3,
        jitter=0.2,
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Valor")


g.figure.suptitle(
    "Distribuição das variáveis por qualidade da prateleira",
    fontsize=14
)

g.figure.subplots_adjust(top=0.92)

g.figure.savefig(
    PASTA_GRAFICOS / "distribuicao_variaveis_shelveloc.png",
    dpi=300
)

plt.close(g.figure)

plt.figure(figsize=(6,5))

sns.boxplot(
    data=dados,
    x="ShelveLoc",
    y="Sales"
)

sns.stripplot(
    data=dados,
    x="ShelveLoc",
    y="Sales",
    color="black",
    alpha=0.4
)

plt.title("Sales por qualidade da prateleira")

plt.savefig(
    PASTA_GRAFICOS / "sales_shelveloc.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

plt.figure(figsize=(6,5))

sns.boxplot(
    data=dados,
    x="Urban",
    y="Sales"
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

colunas = dt.colunas()

g = sns.pairplot(
    dados[colunas],
    hue="ShelveLoc",
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

matriz_cor.round(3).to_csv("../resultados/matriz_correlacao.csv")

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
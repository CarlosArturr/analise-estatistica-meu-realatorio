from statsmodels.stats.anova import anova_lm
import statsmodels.formula.api as smf

import data as dt

modelo_completo = smf.ols(
    "Sales ~ CompPrice + Income + Advertising + Population + Price + ShelveLoc + Age + Education + Urban + US",
    data= dt.extract()
).fit()

print(modelo_completo.summary())

import statsmodels.formula.api as smf

variaveis = [
    "CompPrice",
    "Income",
    "Advertising",
    "Population",
    "Price",
    "ShelveLoc",
    "Age",
    "Education",
    "Urban",
    "US"
]

melhor_aic = float("inf")
melhor_modelo = None

while True:

    resultados = []

    for v in variaveis:

        candidatos = [x for x in variaveis if x != v]

        formula = "Sales ~ " + " + ".join(candidatos)

        modelo = smf.ols(formula, data=dt.extract()).fit()

        resultados.append((modelo.aic, v, modelo))

    resultados.sort()

    aic, removida, modelo = resultados[0]

    if aic < melhor_aic:

        melhor_aic = aic
        melhor_modelo = modelo
        variaveis.remove(removida)

    else:
        break
    
print(melhor_modelo.summary())

import pandas as pd
import numpy as np

modelos = {
    "Completo": modelo_completo,
    "Stepwise": melhor_modelo
}

comparacao = pd.DataFrame({
    "Parâmetros": [len(m.params)-1 for m in modelos.values()],
    "R²": [m.rsquared for m in modelos.values()],
    "R² ajustado": [m.rsquared_adj for m in modelos.values()],
    "RQME": [np.sqrt(m.mse_resid) for m in modelos.values()],
    "AIC": [m.aic for m in modelos.values()],
    "BIC": [m.bic for m in modelos.values()]
}, index=modelos.keys())

print(comparacao.round(3))

anova = anova_lm(melhor_modelo, modelo_completo)
print(anova)
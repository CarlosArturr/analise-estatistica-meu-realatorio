import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from pathlib import Path
from statsmodels.stats.outliers_influence import variance_inflation_factor

arquivo = Path(__file__).resolve().parent.parent / "dados" / "04_Carseats.csv"
df = pd.read_csv(arquivo)

#Comparando o modelo completo com o melhor encontrado
modelo_completo = smf.ols('Vendas ~ PreçoConcorrente + Renda + Publicidade + População + Preço + Idade + Educação + C(LocPrateleira) + C(Urbano) + C(EUA)', data=df).fit()

modelo_melhor = smf.ols('Vendas ~ PreçoConcorrente + Renda + Publicidade + Preço + Idade + C(LocPrateleira)', data=df).fit()

print(modelo_completo.summary())
print(modelo_melhor.summary())

print("AIC Completo: ", modelo_completo.aic)
print("AIC Melhor: ", modelo_melhor.aic)

print("BIC Completo: ", modelo_completo.bic)
print("BIC Melhor: ", modelo_melhor.bic)

#Multicolinearidade(Não possui problemas)
X = modelo_melhor.model.exog
nomes_variaveis = modelo_melhor.model.exog_names

tabela_vif = pd.DataFrame()
tabela_vif["Variavel"] = nomes_variaveis

tabela_vif["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

tabela_vif["VIF"] = tabela_vif["VIF"].round(2)

print("=== DIAGNÓSTICO DE MULTICOLINEARIDADE (VIF) ===")
print(tabela_vif)

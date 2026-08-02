import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

arquivo = Path(__file__).resolve().parent.parent / "dados" / "04_Carseats.csv"
df = pd.read_csv(arquivo)

modelo_melhor = smf.ols('Vendas ~ PreçoConcorrente + Renda + Publicidade + Preço + Idade + C(LocPrateleira)', data=df).fit()

sns.set_theme(style="whitegrid", rc={"grid.color": ".9", "axes.edgecolor": "white"})

influencia = modelo_melhor.get_influence()
n = int(modelo_melhor.nobs)
p = int(modelo_melhor.df_model + 1)

valores_ajustados = modelo_melhor.fittedvalues
residuos = modelo_melhor.resid
residuos_padronizados = influencia.resid_studentized_internal
alavancagem = influencia.hat_matrix_diag
distancia_cook = influencia.cooks_distance[0]

fig, ax = plt.subplots(2, 2, figsize=(12, 10))
cor_ponto = '#4C72B0'
cor_linha = '#A05271' 

#Resíduos × ajustados
sns.residplot(x=valores_ajustados, y=residuos, lowess=True,
              scatter_kws={'alpha': 0.8, 'color': cor_ponto, 's': 25},
              line_kws={'color': cor_linha, 'lw': 2}, ax=ax[0, 0])
ax[0, 0].set_title('Resíduos × ajustados', fontsize=13, fontweight='bold', color='#1A365D', loc='left', pad=25)
ax[0, 0].text(0, 1.02, 'Procure curvatura e formato de funil', transform=ax[0, 0].transAxes, fontsize=9, color='gray')
ax[0, 0].set_xlabel('Valor ajustado')
ax[0, 0].set_ylabel('Resíduo')
ax[0, 0].axhline(0, color='gray', linestyle='--', lw=1)

#QQ-plot com envelope de 95%
residuos_ordenados = np.sort(residuos_padronizados)
p_vals = (np.arange(1, n + 1) - 0.5) / n
quantis_teoricos = stats.norm.ppf(p_vals)

ax[0, 1].scatter(quantis_teoricos, residuos_ordenados, alpha=0.8, color=cor_ponto, s=25)

min_val = np.min([quantis_teoricos.min(), residuos_ordenados.min()])
max_val = np.max([quantis_teoricos.max(), residuos_ordenados.max()])
ax[0, 1].plot([min_val, max_val], [min_val, max_val], color=cor_linha, lw=2)

se_quantis = (1 / stats.norm.pdf(quantis_teoricos)) * np.sqrt((p_vals * (1 - p_vals)) / n)
margem = 1.96 * se_quantis
ax[0, 1].fill_between(quantis_teoricos, quantis_teoricos - margem, quantis_teoricos + margem, 
                      color='#F4E8D1', alpha=0.8, zorder=0)
                      
ax[0, 1].set_title('QQ-plot com envelope de 95%', fontsize=13, fontweight='bold', color='#1A365D', loc='left', pad=25)
ax[0, 1].text(0, 1.02, 'Pontos fora da faixa sugerem desvio de normalidade', transform=ax[0, 1].transAxes, fontsize=9, color='gray')
ax[0, 1].set_xlabel('Quantis teóricos')
ax[0, 1].set_ylabel('Resíduo padronizado')

#Escala-localização
residuos_raiz_abs = np.sqrt(np.abs(residuos_padronizados))
sns.regplot(x=valores_ajustados, y=residuos_raiz_abs, scatter=True, ci=None, lowess=True,
            line_kws={'color': cor_linha, 'lw': 2},
            scatter_kws={'alpha': 0.8, 'color': cor_ponto, 's': 25}, ax=ax[1, 0])
ax[1, 0].set_title('Escala-localização', fontsize=13, fontweight='bold', color='#1A365D', loc='left', pad=25)
ax[1, 0].text(0, 1.02, 'Uma faixa aproximadamente horizontal é desejável', transform=ax[1, 0].transAxes, fontsize=9, color='gray')
ax[1, 0].set_xlabel('Valor ajustado')
ax[1, 0].set_ylabel('$\\sqrt{|Resíduo padronizado|}$')

#Alavancagem e influência
tamanhos_bolhas = 20 + (distancia_cook / np.max(distancia_cook)) * 300 

ax[1, 1].scatter(alavancagem, residuos_padronizados, s=tamanhos_bolhas, alpha=0.7, color=cor_ponto)

ax[1, 1].axhline(y=2, color='gray', linestyle='--', lw=1.2)
ax[1, 1].axhline(y=-2, color='gray', linestyle='--', lw=1.2)

limite_alavancagem = 2 * p / n
ax[1, 1].axvline(x=limite_alavancagem, color='#E69F00', linestyle='--', lw=1.2)

ax[1, 1].set_title('Alavancagem e influência', fontsize=13, fontweight='bold', color='#1A365D', loc='left', pad=25)
ax[1, 1].text(0, 1.02, 'Linha laranja: alavancagem alta; tamanho: distância de Cook', transform=ax[1, 1].transAxes, fontsize=9, color='gray')
ax[1, 1].set_xlabel('Alavancagem')
ax[1, 1].set_ylabel('Resíduo padronizado')

plt.tight_layout()
fig.subplots_adjust(hspace=0.6, top=0.92)
plt.show()
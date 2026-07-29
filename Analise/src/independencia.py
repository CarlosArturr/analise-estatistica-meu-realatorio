import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arquivo = Path(__file__).resolve().parent.parent / "dados" / "04_Carseats.csv"
df = pd.read_csv(arquivo)

modelo_melhor = smf.ols('Sales ~ CompPrice + Income + Advertising + Price + Age + C(ShelveLoc)', data=df).fit()

sns.set_theme(style="whitegrid", rc={"grid.color": ".9", "axes.edgecolor": "white"})

residuos = modelo_melhor.resid
indices = np.arange(len(residuos))

fig, ax = plt.subplots(figsize=(10, 4))
cor_ponto = '#4C72B0'
cor_linha = '#A05271'

ax.plot(indices, residuos, color=cor_ponto, alpha=0.6, lw=1, marker='o', markersize=4)
ax.axhline(0, color='gray', linestyle='--', lw=1.2)

ax.set_title('Resíduos na ordem das observações', fontsize=13, fontweight='bold', color='#1A365D', loc='left', pad=25)
ax.text(0, 1.02, 'Só é informativo sobre dependência se a ordem tiver significado no desenho', transform=ax.transAxes, fontsize=9, color='gray')
ax.set_xlabel('Índice da observação')
ax.set_ylabel('Resíduo')

#O resultado do gráfico confirma indepenência
plt.tight_layout()
plt.show()

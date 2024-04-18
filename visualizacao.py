from sys import argv

import pandas as pd
import seaborn as sns

# Lendo o arquivo com os registros da taxa CDI

df = pd.read_csv('taxa-cdi.csv')

# Salvando o gráfico

grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.get_figure().savefig(f'{argv[1]}.png')
import pandas as pd
import numpy as np

dados = {
    'Valores': [10, 20, 20, 40, 50, 50, 50, 60, 70, 80]
}
df = pd.DataFrame(dados)
print(df)
print()

media = df['Valores'].mean()
print(f"Média: {media}")
print()

desvio_padrao = df['Valores'].std()
print(f"Desvio Padrão: {desvio_padrao}")
print()

soma = df['Valores'].sum()
print(f"Soma: {soma}")


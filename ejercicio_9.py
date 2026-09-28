#Ejercicio 9 — Tarifas y pasajeros destacados

# 1. Calcular el mínimo, el máximo, la media y la mediana de `fare`.
# 2. Mostrar las 10 filas con las tarifas más altas, incluyendo `pclass`, `sex`, `age`, `fare` y `embark_town`.
# 3. Contar cuántas personas tienen tarifa igual a cero.
# 4. Comparar la media con la mediana y explicar qué efecto podrían tener las tarifas muy altas.

# **Pista:** usar `.describe()`, `.median()` y `.sort_values()` o `.nlargest()`.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

minimo = df['fare'].min()
maximo = df['fare'].max()
media = df['fare'].mean()
mediana = df['fare'].median()

print(f"Mínimo: {minimo:.2f}")
print(f"Máximo: {maximo:.2f}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")

top_10_tarifas = df.nlargest(10, 'fare')[['pclass', 'sex', 'age', 'fare', 'embark_town']]
print(top_10_tarifas)

tarifa_cero = (df['fare'] == 0).sum()
print(f"Pasajeros con tarifa 0: {tarifa_cero}")

# La media es más alta que la mediana. Esto indica que hay tarifas muy altas (outliers) que inflan el promedio.
# La mediana no se ve afectada por esos valores extremos y refleja mejor lo que pagó la mayoría de los pasajeros. 
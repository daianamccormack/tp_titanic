# Ejercicio 14 — Edades con NumPy

# 1. Convertir las edades conocidas en un array de NumPy, excluyendo los valores nulos.
# 2. Calcular la edad mínima, máxima, promedio y los percentiles 25, 50 y 75.
# 3. Usar una máscara booleana para obtener las edades entre 18 y 60 años, ambos incluidos.
# 4. Informar cuántas cumplen esa condición y qué porcentaje representan sobre las personas con edad conocida.
# 5. Verificar que el promedio obtenido coincide con `df["age"].mean()` usando `np.isclose()`.

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

edades = df['age'].dropna().to_numpy()

edad_min = edades.min()
edad_max = edades.max()
edad_promedio = edades.mean()

p25, p50, p75 = np.percentile(edades, [25, 50, 75])

print(f"Mínima: {edad_min}, Máxima: {edad_max}, Promedio: {edad_promedio:.2f}")
print(f"Percentiles - 25: {p25}, 50: {p50}, 75: {p75}")

mascara = (edades >= 18) & (edades <= 60)
edades_filtradas = edades[mascara]

cantidad = len(edades_filtradas)
porcentaje = cantidad / len(edades) * 100

print(f"Entre 18 y 60: {cantidad} ({porcentaje:.2f}%)")

print(np.isclose(edad_promedio, df['age'].mean()))
### Ejercicio 11 — Familiares a bordo

# 1. Crear una copia llamada `df_familias` y agregar `tamano_familia = sibsp + parch + 1`.
# 2. Agregar `viaja_solo`, que sea verdadero cuando el tamaño familiar sea 1.
# 3. Comparar `viaja_solo` con la columna `alone` e informar la cantidad de diferencias.
# 4. Calcular la cantidad de pasajeros y el porcentaje de supervivencia según viajen solos o acompañados.

# ` sibsp ` indica hermanos/as y cónyuges a bordo; `parch`, padres/madres e hijos/as. El 1 incluye al propio pasajero.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

df_familias = df.copy()

df_familias['tamano_familia'] = df_familias['sibsp'] + df_familias['parch'] + 1

df_familias['viaja_solo'] = df_familias['tamano_familia'] == 1

diferencias = (df_familias['viaja_solo'] != df_familias['alone']).sum()
print(f"Diferencias con 'alone': {diferencias}")

resumen_solos = df_familias.groupby('viaja_solo').agg(
    cantidad=('survived', 'size'),
    porcentaje_supervivencia=('survived', lambda x: x.mean() * 100)
).round(2)

print(resumen_solos)
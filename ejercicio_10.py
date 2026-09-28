# Ejercicio 10 — Supervivencia por clase y sexo

# 1. Agrupar simultáneamente por `pclass` y `sex`.
# 2. Para cada grupo, calcular la cantidad de pasajeros, la cantidad de sobrevivientes y el porcentaje de supervivencia.
# 3. Ordenar los grupos por porcentaje de supervivencia e identificar el mayor y el menor.
# 4. Escribir una conclusión breve que tenga en cuenta también el tamaño de cada grupo.

# **Pista:** usar `groupby()` con una lista de columnas y `.agg()`. En `survived`, la suma cuenta sobrevivientes y la media multiplicada por 100 expresa el porcentaje.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

resumen_clase_sexo = df.groupby(['pclass', 'sex']).agg(
    pasajeros=('survived', 'size'),
    sobrevivientes=('survived', 'sum'),
    porcentaje_supervivencia=('survived', lambda x: x.mean() * 100)
).sort_values('porcentaje_supervivencia', ascending=False)

print(resumen_clase_sexo)

#Conclusion:
# Las mujeres de primera clase tienen la mayor supervivencia (96.8%).
# Los hombres de tercera clase tienen la menor supervivencia (13.5%).
# En todas las clases, las mujeres sobrevivieron más que los hombres.
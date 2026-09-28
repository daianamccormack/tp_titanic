# Ejercicio 16 — Informe por puerto y exportación

# 1. Crear una copia de `df` y completar los nulos de `embark_town` con `Sin dato`.
# 2. Elaborar una tabla por puerto con cantidad de pasajeros, tarifa promedio y porcentaje de supervivencia.
# 3. Representar el porcentaje de supervivencia por puerto con un gráfico de barras, con eje vertical de 0 a 100.
# 4. Guardar la tabla en `data/resumen_titanic_por_puerto.csv`, incluyendo el puerto como columna y sin exportar el índice.
# 5. Volver a leer el archivo y comprobar que conserva las mismas columnas y cantidad de filas.
# 6. Escribir una conclusión de dos o tres oraciones. Aclarar por qué esta comparación por sí sola no demuestra que el puerto haya causado una diferencia en supervivencia.

# **Pista:** usar `.groupby()`, `.agg()`, `.reset_index()` y `.to_csv(index=False)`.

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

df_puertos = df.copy()

df_puertos['embark_town'] = df_puertos['embark_town'].fillna('Sin dato')

resumen_puertos = df_puertos.groupby('embark_town').agg(
    cantidad=('survived', 'size'),
    tarifa_promedio=('fare', 'mean'),
    porcentaje_supervivencia=('survived', lambda x: x.mean() * 100)
).reset_index().round(2)

print(resumen_puertos)

plt.bar(resumen_puertos['embark_town'], resumen_puertos['porcentaje_supervivencia'])
plt.ylim(0, 100)
plt.title('Porcentaje de supervivencia por puerto')
plt.xlabel('Puerto')
plt.ylabel('% Supervivencia')

ruta_grafico = os.path.join(os.path.dirname(__file__), 'ejercicio_16_grafico.png')
plt.savefig(ruta_grafico, dpi=100)
plt.show()

ruta_csv = os.path.join(os.path.dirname(__file__), 'resumen_titanic_por_puerto.csv')
resumen_puertos.to_csv(ruta_csv, index=False)

verificacion = pd.read_csv(ruta_csv)
print(verificacion.shape == resumen_puertos.shape)
print(list(verificacion.columns) == list(resumen_puertos.columns))

# El puerto de Cherbourg tiene la mayor supervivencia (55.36%).
# Southampton tiene la mayor cantidad de pasajeros (644).
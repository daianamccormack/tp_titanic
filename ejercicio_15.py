# ### Ejercicio 15 — Distribución de edades y tarifas

# 1. Crear una figura con dos subgráficos: un histograma de `age` y un diagrama de caja de `fare`.
# 2. Excluir valores nulos únicamente de la columna utilizada en cada gráfico.
# 3. Agregar títulos y nombres de ejes; en el histograma, elegir una cantidad de intervalos que permita distinguir la distribución.
# 4. Escribir dos observaciones: una sobre las edades más frecuentes y otra sobre las tarifas alejadas de la mayoría. No eliminar valores solo por ser altos.

# **Pista:** usar `plt.subplots(1, 2)`, `.hist()`, `.boxplot()` y `plt.tight_layout()`.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

fig, ejes = plt.subplots(1, 2, figsize=(12, 5))

ejes[0].hist(df['age'].dropna(), bins=20)
ejes[0].set_title('Distribución de edades')
ejes[0].set_xlabel('Edad')
ejes[0].set_ylabel('Frecuencia')

ejes[1].boxplot(df['fare'].dropna())
ejes[1].set_title('Distribución de tarifas')
ejes[1].set_ylabel('Tarifa')

plt.tight_layout()
import os
ruta = os.path.join(os.path.dirname(__file__), 'ejercicio_15_graficos.png')
plt.savefig(ruta, dpi=100)
plt.show()

# Observaciones:
# 1. La mayoría de los pasajeros tienen edades entre 20 y 30 años.
# 2. Hay algunas tarifas que son significativamente más altas que la mayoría.
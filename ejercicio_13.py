### Ejercicio 13 — Clasificación de tarifas con una función

# 1. Definir `clasificar_tarifa(fare)` con estas categorías: `sin dato` si es nula, `gratuita` si vale 0, `económica` si es mayor a 0 y menor a 15, `media` si es mayor o igual a 15 y menor a 50, y `alta` si es mayor o igual a 50.
# 2. Aplicar la función a `fare` y guardar el resultado en una columna `categoria_tarifa` de una copia de `df`.
# 3. Contar los pasajeros de cada categoría y calcular su porcentaje de supervivencia.
# 4. Ordenar los resultados por cantidad de pasajeros usando una función `lambda` como `key` de `sorted()` sobre una lista de tuplas `(categoria, cantidad)`.

# **Pista:** usar `pd.isna()`, condicionales, `.apply()` y `.value_counts()`.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

def clasificar_tarifa(fare):
    if pd.isna(fare):
        return "sin dato"
    elif fare == 0:
        return "gratuita"
    elif fare < 15:
        return "económica"
    elif fare < 50:
        return "media"
    else:
        return "alta"

df_tarifas = df.copy()
df_tarifas['categoria_tarifa'] = df_tarifas['fare'].apply(clasificar_tarifa)

resumen_categorias = df_tarifas.groupby('categoria_tarifa').agg(
    cantidad=('survived', 'size'),
    porcentaje_supervivencia=('survived', lambda x: x.mean() * 100)
).round(2)

print(resumen_categorias)

lista_categorias = list(zip(resumen_categorias.index, resumen_categorias['cantidad']))
lista_ordenada = sorted(lista_categorias, key=lambda x: x[1], reverse=True)

print(lista_ordenada)

# La mayoría de los pasajeros pagaron tarifas "económicas" (520).
# Los que pagaron tarifas "altas" tuvieron mayor supervivencia (61.58%).
# Los de tarifa "gratuita" tuvieron baja supervivencia (13.33%), pero son pocos (15).
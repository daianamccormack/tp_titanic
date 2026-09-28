# ### Ejercicio 7 — Selección y filtros combinados

# 1. Seleccionar las personas de tercera clase (`pclass == 3`) con edad conocida menor a 18 años.
# 2. Mostrar solamente `sex`, `age`, `fare` y `survived`, ordenadas por edad de menor a mayor.
# 3. Informar cuántas personas cumplen las condiciones y qué porcentaje representan sobre el total del dataset.

# **Pista:** combinar condiciones con `&` y encerrar cada condición entre paréntesis; usar `.loc` y `.sort_values()

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

filtro = (df["pclass"] == 3) & (df["age"].notna()) & (df["age"] < 18)
resultado = df.loc[filtro, ["sex", "age", "fare", "survived"]].sort_values("age")

print(resultado)
print(f"Cantidad: {len(resultado)}")
print(f"Porcentaje: {len(resultado) / len(df) * 100:.2f}%")
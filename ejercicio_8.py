# ### Ejercicio 8 — Diagnóstico de valores faltantes

# 1. Crear una tabla con la cantidad y el porcentaje de valores nulos de cada columna.
# 2. Mostrar únicamente las columnas con datos faltantes, ordenadas de mayor a menor porcentaje.
# 3. Crear una copia de `df` y completar las edades ausentes con la mediana de `age`.
# 4. Comparar el promedio de edad antes y después de completar los datos. Explicar por qué podría cambiar.

# **Pista:** usar `.isna()`, `.sum()`, `.copy()` y `.fillna()`. Conservar `df` sin modificar para los demás ejercicios.


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# Calcular cantidad y porcentaje de nulos por columna
nulos = df.isna().sum()
porcentaje_nulos = df.isna().sum() / len(df) * 100

# Crear tabla resumen
tabla_nulos = pd.DataFrame({
    'cantidad': nulos,
    'porcentaje': porcentaje_nulos
})

# Filtrar solo columnas con nulos y ordenar por porcentaje
tabla_faltantes = tabla_nulos[tabla_nulos['cantidad'] > 0].sort_values('porcentaje', ascending=False)

# Copia del DataFrame para no modificar el original
df_copia = df.copy()

# Imputar edades faltantes con la mediana
mediana_age = df['age'].median()
df_copia['age'] = df_copia['age'].fillna(mediana_age)

# Comparar promedios antes y después
promedio_antes = df['age'].mean()
promedio_despues = df_copia['age'].mean()

# Mostrar resultados
print(tabla_faltantes)
print(f"Promedio antes: {promedio_antes:.2f}")
print(f"Promedio después: {promedio_despues:.2f}")

# El promedio cambia porque antes se calculaba con 714 filas (las que tienen edad). 
# Al completar los 177 faltantes con la mediana, esos valores entran al cálculo y el promedio se corre levemente hacia la mediana.


import sqlite3
import pandas as pd

# Crear DB y conectar
conn = sqlite3.connect('ventas.db')

df = pd.read_csv('data\\Sample - Superstore.csv', encoding='latin1')
df.columns = df.columns.str.replace(' ', '_')  # Reemplaza espacios por _
df.to_sql('ventas', conn, if_exists='replace', index=False)

# Hacer consulta
query = "SELECT * FROM ventas WHERE `Order_Date` >= '2025-01-01';"
df_result = pd.read_sql(query, conn)
print(df_result.head())

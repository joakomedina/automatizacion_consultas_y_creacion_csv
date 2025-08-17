import os
import sqlite3
import pandas as pd
import logging
from datetime import datetime

# ------------------------------
# CONFIG
# ------------------------------
BASE_FOLDER = r"C:\Users\joako\OneDrive\Documentos\proyectos_datos\automatizacion"
DB_FILE = os.path.join(BASE_FOLDER, "ventas.db")
TABLE_NAME = "ventas"
CSV_FOLDER = os.path.join(BASE_FOLDER, "csv_export")
FECHA_INICIO = "2025-01-01"

# Crear carpeta si no existe
os.makedirs(CSV_FOLDER, exist_ok=True)

# ------------------------------
# LOGGING
# ------------------------------
logging.basicConfig(
    filename=os.path.join(BASE_FOLDER, "log_ventas.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("--- Inicio del script ---")

try:
    conn = sqlite3.connect(DB_FILE)
    query = f"""
    SELECT *
    FROM {TABLE_NAME}
    WHERE Order_Date >= '{FECHA_INICIO}';
    """
    df = pd.read_sql(query, conn)
    logging.info(f"Consulta ejecutada correctamente. Filas obtenidas: {len(df)}")

    # Guardar CSV con timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    csv_file = os.path.join(CSV_FOLDER, f"ventas_{timestamp}.csv")
    df.to_csv(csv_file, index=False)
    logging.info(f"Archivo CSV generado correctamente: {csv_file}")
    print(f"CSV generado en: {csv_file}")

except Exception as e:
    logging.error(f"Error durante la ejecución: {e}")
    print(f"Error: {e}")

logging.info("--- Fin del script ---")

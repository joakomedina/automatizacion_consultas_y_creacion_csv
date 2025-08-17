# Automatización de consultas con Python y Windows Task Scheduler

Este proyecto muestra cómo **automatizar la ejecución de consultas en una base de datos SQLite** y exportar los resultados en archivos CSV.  
La automatización se logra combinando scripts en Python con el **Programador de Tareas de Windows**.

---

## 📂 Estructura del proyecto

.
├── automatizacion.py # Carga de datos inicial a la base de datos SQLite
├── consultas.py # Consulta y exportación de resultados a CSV
├── ventas.db # Base de datos SQLite generada automáticamente
├── csv_export/ # Carpeta donde se guardan los CSV
│ ├── ventas_20250817_121119.csv
│ ├── ventas_20250817_121624.csv
│ ├── ...
└── README.md # Documentación


---

## ⚙️ Paso 1: Configurar el entorno

1. Clona este repositorio:
   ```bash
   git clone <url-del-repo>
   cd <nombre-del-repo>

2. (Opcional) Crea un entorno virtual:
python -m venv venv
venv\Scripts\activate

3. Instala dependencias:
pip install pandas sqlalchemy

## 📊 Paso 2: Ejecutar los scripts manualmente
1. automatizacion.py
Carga datos desde Sample - Superstore.csv a la base de datos SQLite (ventas.db) y genera la tabla ventas.
2. consultas.py
Consulta las ventas desde 2025-01-01 y exporta los resultados a un CSV con nombre basado en fecha y hora.
📌 Ejemplo de archivo generado:
csv_export/ventas_20250817_121119.csv

⏰ Paso 3: Automatizar con el Programador de Tareas de Windows

El objetivo es que consultas.py se ejecute automáticamente cada cierto tiempo (ejemplo: cada 5 minutos).

### Creación de la tarea programada

1. Abre Programador de Tareas en Windows (taskschd.msc).

2. Haz clic en Crear tarea...

3. En la pestaña General:

- Ponle un nombre: Consulta Ventas Automática

- Selecciona Ejecutar tanto si el usuario inició sesión como si no (si aplica).

4. En la pestaña Desencadenadores:

- Clic en Nuevo...

- Elige "En un horario" → Cada 5 minutos, repetir 4 veces (o como prefieras).

5. En la pestaña Acciones:

- Acción: Iniciar un programa

- Programa o script: "C:\Program Files\Python312\python.exe"
- Agregar argumentos: "C:\Users\tuUsuario\OneDrive\Documentos\proyectos_datos\automatizacion\consultas.py"
- Iniciar en (opcional, pero recomendado): C:\Users\tuUsuario\OneDrive\Documentos\proyectos_datos\automatizacion

6. Guarda la tarea e ingresa la contraseña de tu usuario si te lo pide.

#### Resultados esperados: 
En la carpeta csv_export/
ventas_20250817_121119.csv
ventas_20250817_121624.csv
ventas_20250817_122129.csv

✅ Conclusiones

automatizacion.py prepara los datos en la base de datos.

consultas.py consulta y exporta resultados.

El Programador de Tareas de Windows asegura que el proceso corra de manera automática, sin intervención manual.

Este flujo es un ejemplo práctico de automatización de procesos ETL (Extract, Transform, Load) con Python.
import os
import sqlite3
from dotenv import load_dotenv

# Cargar configuración desde .env
load_dotenv()

SQLITE_DIR = os.getenv("SQLITE_DIR")

connection: sqlite3.Connection | None = None

if not SQLITE_DIR:
    print("FATAL: Falta la variable SQLITE_DIR en el archivo .env")
else:
    try:
        parent_dir = os.path.dirname(os.path.abspath(SQLITE_DIR))
        os.makedirs(parent_dir, exist_ok=True)
        connection = sqlite3.connect(SQLITE_DIR)
        connection.row_factory = sqlite3.Row
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                status TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
            """
        )
        connection.commit()
        
    except Exception as e:
        print(f"ERROR: No se pudo inicializar SQLite en {SQLITE_DIR}: {e}")
        connection = None

"""
Script para migrar la base de datos agregando campos de cliente a la tabla orders
"""

import os
import sys
import sqlite3
from pathlib import Path

# Agregar la carpeta app al path
sys.path.insert(0, str(Path(__file__).parent / 'app'))

def migrate_database():
    """Migra la BD agregando las columnas de cliente a la tabla orders"""

    db_path = Path(__file__).resolve().parent / "instance" / "sanvicentino.db"

    # Si la BD no existe aún, no hay nada que migrar
    if not db_path.exists():
        print("Base de datos no existe aún. Se creará en la próxima ejecución.")
        return

    print(f"Verificando base de datos en: {db_path}")

    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Obtener información de la tabla orders
        cursor.execute("PRAGMA table_info(orders)")
        columns = [row[1] for row in cursor.fetchall()]

        columns_to_add = [
            ('nombre_cliente', 'VARCHAR(255)'),
            ('direccion_entrega', 'TEXT'),
            ('referencia', 'TEXT')
        ]

        for column_name, column_type in columns_to_add:
            if column_name not in columns:
                print(f"Columna '{column_name}' no encontrada. Agregando...")
                cursor.execute(f"ALTER TABLE orders ADD COLUMN {column_name} {column_type}")
                conn.commit()
                print(f"✓ Columna '{column_name}' agregada exitosamente")
            else:
                print(f"✓ La columna '{column_name}' ya existe en la tabla")

        conn.close()
        print("✓ Migración completada exitosamente")

    except sqlite3.OperationalError as e:
        print(f"✗ Error al migrar: {str(e)}")
        print("La base de datos podría estar corrupta. Considera eliminarla y reiniciar.")
    except Exception as e:
        print(f"✗ Error inesperado: {str(e)}")

if __name__ == "__main__":
    migrate_database()
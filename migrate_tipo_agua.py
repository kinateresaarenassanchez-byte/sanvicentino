"""
Script para agregar la columna tipo_agua a la tabla products
Ejecutar después de actualizar el modelo
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from run import app, db

def add_tipo_agua_column():
    """Agrega la columna tipo_agua a la tabla products"""
    with app.app_context():
        try:
            # Usar SQLAlchemy para agregar la columna
            from sqlalchemy import text

            # Verificar si la columna ya existe
            result = db.session.execute(text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'products' AND column_name = 'tipo_agua'
            """))

            if result.fetchone():
                print("✓ La columna 'tipo_agua' ya existe")
                return

            # Agregar la columna
            db.session.execute(text("""
                ALTER TABLE products ADD COLUMN tipo_agua VARCHAR(100)
            """))

            db.session.commit()
            print("✓ Columna 'tipo_agua' agregada exitosamente a la tabla products")

        except Exception as e:
            db.session.rollback()
            print(f"✗ Error al agregar la columna: {e}")

if __name__ == "__main__":
    print("Agregando columna tipo_agua a la tabla products...")
    add_tipo_agua_column()
    print("Migración completada.")
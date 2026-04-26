"""
Script de prueba para crear un producto con tipo de agua
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from run import app, db
from models import Product

def test_tipo_agua():
    """Crea un producto de prueba con tipo de agua"""
    with app.app_context():
        try:
            # Crear producto de prueba
            test_product = Product(
                nombre="Agua San Vicentino - Prueba",
                descripcion="Producto de prueba para verificar tipo de agua",
                precio=3.50,
                categoria="Agua",
                tipo_agua="Bidon de 20L",
                imagen="https://via.placeholder.com/300x300?text=Agua+Prueba",
                stock=50,
                publicado=True
            )

            db.session.add(test_product)
            db.session.commit()

            print("✅ Producto de prueba creado exitosamente")
            print(f"ID: {test_product.id}")
            print(f"Nombre: {test_product.nombre}")
            print(f"Categoría: {test_product.categoria}")
            print(f"Tipo de Agua: {test_product.tipo_agua}")
            print(f"Publicado: {test_product.publicado}")

        except Exception as e:
            db.session.rollback()
            print(f"✗ Error al crear producto de prueba: {e}")

if __name__ == "__main__":
    print("Creando producto de prueba con tipo de agua...")
    test_tipo_agua()
    print("Prueba completada.")
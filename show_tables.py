import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from run import app, db
from models import Product, User, Cart, CartItem, Order, OrderItem, Payment

with app.app_context():
    print('=' * 100)
    print('📊 CONTENIDO DE LAS TABLAS DE LA BASE DE DATOS')
    print('=' * 100)

    # Tabla Products
    print('\n🏷️  TABLA: PRODUCTS')
    print('-' * 80)
    products = Product.query.all()
    if products:
        print(f'{"ID":<3} {"NOMBRE":<25} {"PRECIO":<10} {"CATEGORIA":<15} {"STOCK":<8} {"PUBLICADO":<12}')
        print('-' * 80)
        for p in products:
            publicado = '✅ Sí' if p.publicado else '❌ No'
            nombre = p.nombre[:24] if len(p.nombre) > 24 else p.nombre
            categoria = p.categoria[:14] if p.categoria and len(p.categoria) > 14 else (p.categoria or 'N/A')
            print(f'{p.id:<3} {nombre:<25} S/.{p.precio:<8.2f} {categoria:<15} {p.stock:<8} {publicado:<12}')
        print(f'\n📈 Total de productos: {len(products)}')
    else:
        print('No hay productos registrados.')

    # Tabla Users
    print('\n👤 TABLA: USERS')
    print('-' * 60)
    users = User.query.all()
    if users:
        print(f'{"ID":<3} {"USERNAME":<15} {"EMAIL":<25} {"ADMIN":<8} {"CREATED":<12}')
        print('-' * 60)
        for u in users:
            admin = '✅ Sí' if u.is_admin else '❌ No'
            email = u.email[:24] if len(u.email) > 24 else u.email
            created = u.created_at.strftime('%Y-%m-%d') if u.created_at else 'N/A'
            print(f'{u.id:<3} {u.username[:14]:<15} {email:<25} {admin:<8} {created:<12}')
        print(f'\n👥 Total de usuarios: {len(users)}')
    else:
        print('No hay usuarios registrados.')

    # Tabla Cart
    print('\n🛒 TABLA: CART')
    print('-' * 50)
    carts = Cart.query.all()
    if carts:
        print(f'{"ID":<3} {"USER_ID":<8} {"ITEMS":<8} {"TOTAL":<10} {"CREATED":<12}')
        print('-' * 50)
        for c in carts:
            total = f'S/.{c.get_total():.2f}'
            created = c.created_at.strftime('%Y-%m-%d') if c.created_at else 'N/A'
            item_count = c.get_item_count()
            print(f'{c.id:<3} {c.user_id:<8} {item_count:<8} {total:<10} {created:<12}')
        print(f'\n🛒 Total de carritos: {len(carts)}')
    else:
        print('No hay carritos activos.')

    # Tabla Orders
    print('\n📦 TABLA: ORDERS')
    print('-' * 70)
    orders = Order.query.all()
    if orders:
        print(f'{"ID":<3} {"ORDER_NUM":<12} {"USER_ID":<8} {"TOTAL":<10} {"STATUS":<10} {"PAYMENT":<12}')
        print('-' * 70)
        for o in orders:
            order_num = o.order_number[:11] if len(o.order_number) > 11 else o.order_number
            total = f'S/.{o.total:.2f}'
            payment = o.payment_method[:11] if o.payment_method else 'N/A'
            print(f'{o.id:<3} {order_num:<12} {o.user_id:<8} {total:<10} {o.status:<10} {payment:<12}')
        print(f'\n📦 Total de órdenes: {len(orders)}')
    else:
        print('No hay órdenes registradas.')

    print('\n' + '=' * 100)
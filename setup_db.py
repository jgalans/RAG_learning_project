import sqlite3
import pandas as pd

# 1. Conectar (o crear) la base de datos
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 2. Crear las tablas con SQL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id_categoria INTEGER PRIMARY KEY,
        nombre_categoria TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        descripcion TEXT,
        precio FLOAT,
        stock INTEGER,
        id_categoria INTEGER,
        FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria)
    )
''')

# 3. Datos de prueba con el "error" del símbolo €
datos_productos = {
    'nombre': ['Camiseta Eco', 'Botas Trekking', 'Gorra Running'],
    'descripcion': [
        'Algodón 100% orgánico, fresca para el verano.',
        'Cuero resistente, impermeables y cálidas.',
        'Material técnico transpirable, color neón.'
    ],
    'precio_texto': ['25.0€', '89.0€', '15.0€'],
    'stock': [50, 12, 45],
    'id_categoria': [1, 2, 1]
}

df = pd.DataFrame(datos_productos)

# 4. Tu lógica de limpieza
df['precio'] = df['precio_texto'].str.replace('€', '').astype(float)
df = df.drop(columns=['precio_texto']) # Borramos la columna sucia

# 5. Cargar datos a SQL
df.to_sql('productos', conn, if_exists='append', index=False)

print("✅ Base de datos creada y datos cargados con éxito.")
conn.close()
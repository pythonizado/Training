import pandas as pd
import random
from pathlib import Path

def generate_product_name():
    return random.choice([
        'Filete de res', 'Puré de papas', 'Pasta carbonara', 'Pollo al curry',
        'Paella de mariscos', 'Ensalada César', 'Sushi de salmón', 'Tacos',
        'Hamburguesa', 'Ceviche', 'Risotto', 'Ramen', 'Bistec de atún',
        'Ensalada de algas', 'Salsa de tomate', 'Pizza margarita',
        'Salmón a la plancha', 'Empanadas', 'Lasagna', 'Chuletas de cordero'
    ])

def generate_random_name():
    return random.choice([
        "Alejandro", "Beatriz", "Carlos", "Diana", "Eduardo", "Fernanda",
        "Gabriel", "Helena", "Iván", "Julieta", "Laura", "Manuel", "Natalia",
        "Oscar", "Patricia", "Rafael", "Sofía", "Tomás", "Valeria", "Andrés",
        "Blanca", "Cristian", "Daniela", "Enrique"
    ])

def generate_phone_number():
    return f"09{random.randint(1000000, 9999999)}"

def generate_price():
    return random.randint(200, 800)

def generate_tipo_producto():
    return random.choice([
        "Comida Mediterránea", "Comida Asiática", "Comida Mexicana", "Comida Italiana"
    ])

def generate_quejas():
    return random.choice(["Sí", "No"])

# Crear un DataFrame con 70 registros
data = {
    "Producto": [generate_product_name() for _ in range(70)],
    "Tipo_Producto": [generate_tipo_producto() for _ in range(70)],
    "Precio": [generate_price() for _ in range(70)],
    "Mas_de_500_pedidos": [random.choice(["Sí", "No"]) for _ in range(70)],
    "Comensal": [generate_random_name() for _ in range(70)],
    "Cel_Comensal": [generate_phone_number() for _ in range(70)],
    "Quejas": [generate_quejas() for _ in range(70)]
}

# Crear el DataFrame
df_productos = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
file_path = Path.home() / 'Desktop' / 'Python' / 'generarTablas' / 'comidaNueva.xlsx'
df_productos.to_excel(file_path, index=False)

print(f"Archivo guardado en: {file_path}")
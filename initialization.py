import os

import dotenv
import psycopg2
from psycopg2 import Error


try:
    # Parámetros de conexión
    postgres_uri = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(postgres_uri)

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Verificar si ya existe el rol 'SUPERADMIN'
    cursor.execute("SELECT id FROM role WHERE name = %s", ('SUPERADMIN',))
    role_id = cursor.fetchone()

    if role_id is None:  # Si no existe, entonces insertar
        # Role creation
        cursor.execute(
            "INSERT INTO role (name) VALUES (%s)",
            ('SUPERADMIN', )
        )

        # Role operation creation
        cursor.executemany(
            "INSERT INTO role_operation (name, module, role_id) VALUES (%s, %s, %s)",       
            [
                ('CREATE', 'USER', 1),
                ('READ', 'USER', 1),
                ('UPDATE', 'USER', 1),

                ('CREATE', 'ROLE', 1),
                ('READ', 'ROLE', 1),
                ('UPDATE', 'ROLE', 1),

                ('CREATE', 'ROLE_OPERATION', 1),
                ('READ', 'ROLE_OPERATION', 1),
                ('UPDATE', 'ROLE_OPERATION', 1),
            ]
        )

    # Verificar si ya existe el usuario 'SUPERADMIN'
    cursor.execute("SELECT id FROM \"user\" WHERE email = %s", ('SUPERADMIN',))
    user_id = cursor.fetchone()

    if user_id is None:  # Si no existe, entonces insertar
        # User Creation
        cursor.execute(
            "INSERT INTO \"user\" (email, password, role_id) VALUES (%s, %s, %s)",
            ('SUPERADMIN', '$2b$12$TwlD8vZ8ZXSIhzBetBswNu3WxvGk0HbsqaLwzC7m35ILmH6gJDY.e', 1)
        )

    # Commit changes to store them in DB
    connection.commit()

    # Cerrar el cursor y la conexión
    if connection:
        cursor.close()
        connection.close()

except (Exception, Error) as error:
    print("Error al conectar a PostgreSQL:", error)


os.remove(__file__)

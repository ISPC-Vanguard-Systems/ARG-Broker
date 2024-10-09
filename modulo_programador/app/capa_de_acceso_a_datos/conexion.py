import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        """Establece una conexión con la base de datos."""
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="tu_usuario",
                password="tu_contraseña",
                database="nombre_base_datos"
            )
            if self.conexion.is_connected():
                print("Conexión establecida con éxito")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False
        return True

    def confirmar(self):
        """Confirma la transacción actual."""
        if self.conexion:
            self.conexion.commit()
            print("Transacción confirmada (commit)")

    def revertir(self):
        """Revierte la transacción actual."""
        if self.conexion:
            self.conexion.rollback()
            print("Transacción revertida (rollback)")

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

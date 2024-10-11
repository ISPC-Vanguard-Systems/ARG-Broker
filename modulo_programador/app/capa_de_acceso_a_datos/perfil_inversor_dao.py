from conexion import Conexion
from modelo import PerfilInversor

class PerfilInversorDao:
    def __init__(self):
        self.conexion = Conexion()

    #crear nuevo perfil de inversor
    def crear_perfil(self, perfil: PerfilInversor):
        with self.conexion.establecer_conexion() as cursor:
            query = """INSERT INTO perfil_inversor (nombre, hashed_password, variacion_minima_admitida, variacion_maxima_admitida) 
                       VALUES (%s, %s, %s, %s)"""

            cursor.execute(query, (perfil.get_nombre(), perfil.get_hashed_password(),
                                   perfil.get_variacion_minima(), perfil.get_variacion_maxima()))
            self.conexion.commit()

    #obtener un perfil por ID
    def obtener_perfil(self, id_perfil: int) -> PerfilInversor:
        with self.conexion.establecer_conexion() as cursor:
            query = "SELECT * FROM perfil_inversor WHERE id_perfil_inversor = %s"
            cursor.execute(query, (id_perfil,))

            resultado = cursor.fetchone()
            if resultado:
                return PerfilInversor(*resultado)#el * puede manejar un tupla si es necesario
            return None

    def actualizar_perfil(self, perfil: PerfilInversor):
        with self.conexion.establecer_conexion() as cursor:
            query = """UPDATE perfil_inversor 
                       SET nombre = %s, hashed_password = %s, variacion_minima_admitida = %s, variacion_maxima_admitida = %s 
                       WHERE id_perfil_inversor = %s"""
            cursor.execute(query, (perfil.get_nombre(), perfil.get_hashed_password(),
                                   perfil.get_variacion_minima(), perfil.get_variacion_maxima(),
                                   perfil.get_id_perfil()))
            self.conexion.commit()

    def eliminar_perfil(self, id_perfil: int):
        with self.conexion.establecer_conexion() as cursor:
            query = "DELETE FROM perfil_inversor WHERE id_perfil_inversor = %s"
            cursor.execute(query, (id_perfil,))
            self.conexion.commit()





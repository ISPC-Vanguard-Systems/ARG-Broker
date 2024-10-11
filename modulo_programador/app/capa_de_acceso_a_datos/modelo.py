class PerfilInversor:
    def __init__(self, id_perfil, nombre, hashed_password, variacion_minima, variacion_maxima):
        self.__id_perfil = id_perfil
        self.__nombre = nombre
        self.__hashed_password = hashed_password
        self.__variacion_minima = variacion_minima
        self.__variacion_maxima = variacion_maxima

    #Getters
    def get_id_perfil(self):
        return self.__id_perfil

    def get_nombre(self):
        return self.__nombre

    def get_hashed_password(self):
        return self.__hashed_password

    def get_variacion_minima(self):
        return self.__variacion_minima

    def get_variacion_maxima(self):
        return self.__variacion_maxima

    #Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_hashed_password(self, hashed_password):
        self.__hashed_password = hashed_password

    def set_variacion_minima(self, variacion_minima):
        self.__variacion_minima = variacion_minima

    def set_variacion_maxima(self, variacion_maxima):
        self.__variacion_maxima = variacion_maxima

    def __repr__(self):
        return (f"PerfilInversor(id_perfil={self.__id_perfil}, nombre='{self.__nombre}', "
                f"variacion_minima={self.__variacion_minima}, variacion_maxima={self.__variacion_maxima})")

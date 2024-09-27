class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

# Con este metodo puedo pasar el metodo como si fuese atributo

mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo
# 'valor_atributo'

# Esto hace parte del concepto de encapsulamiento, por ello tambien se hace uso de getters y setters

class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != "":
            print("Modificando el valor")
            self.__mi_atributo = valor
        else:
            print("Error está vacío")

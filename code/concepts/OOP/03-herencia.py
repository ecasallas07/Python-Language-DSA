

class Padre():


    def __init__(self):
        print('Father initialization')


class Hijo(Padre):
    pass



# para ver la herencia de Hijo
print(Hijo.__bases__)


# --------------- Example

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10) # heredo el constructor de Animal
mi_perro.describeme() # heredo el metodo
# Soy un Animal del tipo Perro


#------------- uso de super()

class Anial:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perra(Animal):
    def __init__(self, especie, edad, dueño):
        # Alternativa 1 --> crear un constructor para agregar raza
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2 --> mejor opcion por el super()
        super().__init__(especie, edad)
        self.dueño = dueño

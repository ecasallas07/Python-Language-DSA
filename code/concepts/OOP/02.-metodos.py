# uso de decoradores para modificar el comportamiento de un metodo

class Book:

    def __init(self,title,author):
        self.title = title
        self.author = author


    def prestar(self,name):
        self.name = name

    @classmethod
    def class_metodo(cls,):
        print(f"Metodo de clase ")

    @staticmethod
    def metodo_estatico():
        print(f"Metodo estatico")


# Metodo de clase
# Los metodos de clase no pueden acceder a los atributos de la instancia
# modifican los atributos de la clase
print(Book.class_metodo())

# Metodo estatico
# no pueden modificar el estado ni de la clase ni de la instancia
Book.metodo_estatico()

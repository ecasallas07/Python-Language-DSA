'''
 Fundamentals OOP

 Paradigma de progrmacion introducido en los 70

 Clase -> atributos (caracteristicas de las clases)
 Clase -> metodos (funcionalidades de las clases)

La programación orientada a objetos está basada en 6 principios o pilares básicos:

Herencia
Cohesión
Abstracción
Polimorfismo
Acoplamiento
Encapsulamiento


Las clases pueden tener tipos, y estos tipos pasan a ser objetos


TODO: Quedamos en programacion orientada a objetos

'''
class Perro:

    especie= 'mamifero' # atributo de la clase

    # self representa la instancia o la clase y siempre debe ser llamada
    def __init__(self,name,raza): # constructor
        self.name = name # Atributos de instancia que pertenecen a la clase o al objeto
        self.raza = raza

    def ladra(self):
        print('Guau')

    def camina(self, pasos):
        print(f"Camina: {pasos} pasos")



# intanciar clase para a ser objeto
mi_perro = Perro('pooky','gato')  # Objeto
print(mi_perro.name) # De esta forma llamo un atributo de instancia
print(Perro.especie) # Llamar atributo de clase, no necesita metodo

mi_perro.camina(10) # Camina: 10

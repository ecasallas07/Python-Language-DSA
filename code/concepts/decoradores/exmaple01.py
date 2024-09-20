'''
Decoradores
Los decoradores son funciones que modifican el comportamiento de otras funciones



'''


def di_hola():
    print("Hola")

f1 = di_hola() # Llama a la función --> de esta forma llama la funcion
f2 = di_hola   # Asigna a f2 la función --> Pero de esta forma asigna esa funcion a la variable

print(f1)      # None, di_hola no devuelve nada
print(f2)      # <function di_hola at 0x1077bf158>

#f1()          # Error! No es válido
f2()           # Llama a f2, que es di_hola()

del f2         # Borra el objeto que es la función
#f2()          # Error! Ya no existe

di_hola()      # Ok. Sigue existiendo




import time
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}")
        return c
    return funcion_medida


@mide_tiempo
def repirte_funcion(funcion, entrada):
    return [funcion(entrada) for i in range(10000000)]

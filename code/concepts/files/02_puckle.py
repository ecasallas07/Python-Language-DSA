import pickle


# Conceptos usados
# serializacion: Convertir un objeto de python (listas,diccionarios,instancias de clases) en una secuencia de bytes, y guardar en un archivo prar trasmitir
# deserializacion: El proceso inverso


# En ingles pickling en serializar



#serializar
data = {"name": "Esteban","age":24}

with open('data.pickle','wb') as file:
    pickle.dump(data, file)
    
    
#desserializar    
with open('data.pickle','rb') as file:
    data = pickle.load(file)

print(data)    



    
    
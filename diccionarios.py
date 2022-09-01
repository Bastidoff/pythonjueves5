diccionario={
    'nombre':'Daniel',
    'edad':37,
    'estatura':1.80,
    'ocupación':'astronauta'
}

print(diccionario)
#forma de acceder a atributos y valores de forma individual
print(diccionario['nombre'])
#otra, con get
print(diccionario.get('edad'))

#acceder a TODOS los atributos y valores de un diccionario al mismo tiempo
#podemos RECORRER un diccionario

for clave,valor in diccionario.items():
    print(clave, valor)

#AGREGAR desde el código una propiedad más
diccionario['desayuno']=True

print(diccionario)

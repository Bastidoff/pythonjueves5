opcion=100

print("*****Empanadas Inteligentes****")
print("0. Salir")
print("1. Agregar Clientes")
print("2. Mostrar Clientes")
print("3. Buscar un CLIENTE por cédula")
#hacer otra opción REMOVER CLIENTE POR CEDULA



clientes=[]

while opcion!=0:
    cliente={}
    #pedimos la opción deseada
    opcion=int(input("Ingrese la opción deseada: "))
    if opcion==1:
        cliente['cedula']=input("Digite su cédula: ")
        cliente['nombre']=input("Digite su nombre: ")  
        clientes.append(cliente)      
    elif opcion==2:
        print(clientes)
    elif opcion==3:
        cedulaBusqueda=input("Ingrese la cédula que desea buscar: ")
        encontrado=""
        for cliente in clientes:
            if cliente['cedula']== cedulaBusqueda:
                encontrado=f"Cliente encontrado: {cliente['cedula']}"
            else:
                encontrado="Cliente NO encontrado"
        print (encontrado)
    elif opcion==0:
        break
    else:
        print("Ingrese una opción válida.")
else:
    print("ADIÓS")


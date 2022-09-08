opcion=100

print("*****Empanadas Inteligentes****")
print("0. Salir")
print("1. Agregar Clientes")
print("2. Mostrar Clientes")
print("3. Buscar un CLIENTE por cédula")
print("4. Quitar Cliente")
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
                encontrado=f"Cliente encontrado: {cliente['cedula']} {cliente['nombre']}"
                break
            else:
                encontrado="Cliente NO encontrado"
        print (encontrado)
    
    elif opcion==4:
        cedulaEliminar=input("Ingrese la cédula del cliente que desea eliminar: ")
        eliminado=""
        for cliente in clientes:
            if cliente['cedula']== cedulaEliminar:
                eliminado = f"El cliente {cliente['nombre']} con cédula {cliente['cedula']} se eliminó correctamente."
                clientes.remove(cliente)
                break
            else:
                eliminado=f"No existe ningún cliente con la cédula {cedulaEliminar}. No se eliminó ningún registro."
        print(eliminado)
            
    elif opcion==0:
        break
    else:
        print("Ingrese una opción válida.")
else:
    print("ADIÓS")


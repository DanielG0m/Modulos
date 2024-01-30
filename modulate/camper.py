def create():
    print("Camper se guardo ")

def read():
    print("Datos del camper ")

def update():
    print("Camper actualizado ")

def delete():
    print("Camper eliminado")

def menu():
    print("""
#################################
#        Menu del camper        #
#################################
          """)
    print("1. Guardar\n2. Buscar\n3. Actualizar\n4. Eliminar")
    while True:
        try:
            opc=int(input())
            break
        except ValueError:
            print("Ingrese un dato valido")
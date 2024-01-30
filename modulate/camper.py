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
    menu= ["Guardar","Buscar","Actualizar","Eliminar"]
    print(".".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
    while True:
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                print("x")
                break
        except ValueError:
            print("Ingrese un dato valido")

def masa(pizza):
    
    opcion = input("""
Selecciona la base: 
1. Masa Tradicional.
2. Masa Delgada.
3. Masa con Bordes de Queso.
Opción: """)

    if opcion == "1":
        pizza["masa"] = "Masa Tradicional"

    elif opcion == "2":
        pizza["masa"] = "Masa Delgada"

    elif opcion == "3":
        pizza["masa"] = "Masa con Bordes de Queso"

    else:
        print("Opción no válida.")
        return

   




def elegir_salsa(pizza):

    opcion = input("""
Selecciona las salsas:
                   
1. Salsa de Tomate.
2. Salsa Alfredo.
3. Salsa Barbecue.
4. Salsa Pesto.
Opcion: """)
    
    if opcion == "1":
        pizza["salsa"] = "Salsa de Tomate"

    elif opcion == "2":
        pizza["salsa"] = "Salsa Alfredo"

    elif opcion == "3":
        pizza["salsa"] = "Salsa Barbecue"
    
    elif opcion == "4":
        pizza["salsa"] = "Salsa Pesto"

    else:
        print("Opción no válida.")
        return
    

   
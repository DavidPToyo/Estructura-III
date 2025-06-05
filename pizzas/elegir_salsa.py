


def elegir_salsa(pizza):
    salsa = ["1", "2", "3", "4"]

    opcion = int(input("""
Selecciona las salsas:
                   
1. Salsa de Tomate.
2. Salsa Alfredo.
3. Salsa Barbecue.
4. Salsa Pesto.
"""))
    
    if opcion == salsa[0]:
        pizza["salsa"] = "Salsa de Tomate"
        print(f"La {pizza[salsa]} agregada correctamente. ")
    
    elif opcion == salsa[1]:
        pizza["salsa"] = "Salsa Alfredo"
        print(f"La {pizza[salsa]} agregada correctamente. ")
    
    elif opcion == salsa[2]:
        pizza["salsa"] = "Salsa Barbecue"
        print(f"La {pizza[salsa]} agregada correctamente. ")
    
    elif opcion == salsa[3]:
        print(f"La {pizza[salsa]} agregada correctamente. ")

    else:
        print("Opción no valida")

    return pizza
def masa(pizza):
    base = ["1","2","3"]
    
    opcion = int(input("""
selecciona la base: 
1. Masa Tradicional.
2. Masa Delgada.
3. Masa con Bordes de Queso.
"""))
    
    

    if opcion == base[0]:
        pizza["base"] = "Masa Tradicional"
        print(f"{pizza[base]} agregada correctamente. ")

    elif opcion == base[1]:
        pizza["base"] = "Masa Delgada"
        print(f"{pizza[base]} agregada correctamente. ")

    elif opcion == base[2]:
        pizza["base"] = "Masa con Bordes de Queso"
        print(f"{pizza[base]} agregada correctamente. ")

    else:
        print("Opción no valida")

    return pizza
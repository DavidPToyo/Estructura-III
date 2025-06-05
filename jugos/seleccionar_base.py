def seleccionar_base(vaso):
    base = ["1","2"]
    
    opcion = int(input("""
selecciona la base: 
1. Para agua.
2. Para leche
"""))
    
    

    if opcion == base[0]:
        vaso["base"] = "agua"
        print(f"base de {vaso[base]} agregadacorrectamente...")
    elif opcion == base[1]:
        vaso["base"] = "leche"

    else:
        print("Opción no valida")

    return vaso
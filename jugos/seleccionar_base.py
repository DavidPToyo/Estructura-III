def seleccionar_base(vaso):
    base = ["agua","leche"]

    input("""
selecciona la base: 
1. Para agua.
2. Para leche
""")
    
    if eleccion in ["1","2"]:
        if eleccion == "1":
            return "agua"

    else:
        print("opcion invalida")
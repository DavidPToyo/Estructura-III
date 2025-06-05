


def elegir_endulzante(vaso):
    endulzante = ["1", "2"]

    opcion = int(input("""
Selecciona los endulzantes:
                   
1. Para Azucar.
2. Para Miel.
"""))
    
    if opcion == endulzante[0]:
        vaso["endulzante"] = "Azucar"
        print(f"Tipo de endulzante: {vaso[endulzante]} agregadacorrectamente...")
    
    elif opcion == endulzante[1]:
        vaso["endulzante"] = "Miel"
        print(f"Tipo de endulzante: {vaso[endulzante]} agregadacorrectamente...")

    else:
        print("Opción no valida")

    return vaso
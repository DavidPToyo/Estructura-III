def agregar_ingredientes(pizza):
    
    ingredientes = {
        1: "Tomate", 
        2: "Champiñones", 
        3: "Aceituna",
        4: "Cebolla",
        5: "Pollo",
        6: "Jamón",
        7: "Carne",
        8: "Tocino",
        9: "Queso"
}
    print("Las opciones de ingredientes son los siguientes: ")
    for k, v in ingredientes.items():
       print(f"{k}.-{v}")
    
    opcion = int(input(": "))

    if opcion in ingredientes:
        ingrediente = ingredientes[opcion]
        pizza["ingredientes"].append(ingrediente)
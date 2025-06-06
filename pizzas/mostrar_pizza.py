def mostrar_pizza(pizza):

    print("Tu Pizza es de: ")
    print(f"Masa: {pizza.get('masa', 'No seleccionada')}")
    print(f"Salsa: {pizza.get('salsa', 'No seleccionada')}")

    ingredientes = pizza.get('ingredientes', [])
    if ingredientes:
        print("Ingredientes:")
        for i, ingrediente in enumerate(ingredientes, 1):
            print(f"  {i}. {ingrediente}")
    else:
        print("Ingredientes: No se han agregado ingredientes.")
   


def quitar_ingrediente(pizza):
   ingredientes = pizza["ingredientes"]
   
   if not ingredientes:
      print("La pizza no tiene ingredientes para quitar.")

   print("Ingredientes actuales en tu pizza: ")
   for i, ing in enumerate(ingredientes):
      print(f"{i + 1}. {ing}")
    
   opcion = int(input("Elige el número del ingrediente que quieres quitar: ")) - 1

   if 0 <= opcion < len(ingredientes):
      ingrediente = ingredientes[opcion]
      pizza["ingredientes"].remove(ingrediente)
      print(f"{ingrediente} ha sido eliminado de tu pizza.")
   else:
      print("Opción fuera de rango.")

    
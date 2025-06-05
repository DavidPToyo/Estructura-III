from pizzas.menu import menu
from pizzas.base_pizza import base_pizza
from pizzas.seleccionar_base import masa
from pizzas.elegir_salsa import elegir_salsa
from pizzas.agregar_ingredientes import agregar_ingredientes
from pizzas.quitar_ingrediente import quitar_ingrediente

def main():
    
    pizza = base_pizza()

    while True:
        menu()
        opcion = input("opcion: ")

        if opcion == "1": 
            masa(pizza)
            print(pizza)
            
        elif opcion == "2":
            elegir_salsa(pizza)
            print(pizza)

        elif opcion == "3":
            agregar_ingredientes(pizza)
            print(pizza)
        
        elif opcion == "4":
            quitar_ingrediente(pizza)
            print(pizza)
        
        elif opcion == "5":
            print("5")
        
        else:
            print("salir")

if __name__ == "__main__":
    main()
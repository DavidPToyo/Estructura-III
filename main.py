from jugos.menu import menu
from jugos.crear_bebida import crear_bebida
from jugos.seleccionar_base import seleccionar_base
from jugos.elegir_endulzante import elegir_endulzante
from jugos.agregar_frutas import agregar_fruta
from jugos.quitar_frutas import quitar_fruta

def main():
    
    vaso = crear_bebida()

    while True:
        menu()
        opcion = input("opcion: ")

        if opcion == "1": 
            seleccionar_base(vaso)
            print(vaso)
            
        elif opcion == "2":
            elegir_endulzante(vaso)
            print(vaso)
        elif opcion == "3":
            agregar_fruta(vaso)
            print(vaso)
        
        elif opcion == "4":
            quitar_fruta(vaso)
        
        elif opcion == "5":
            print("5")
        
        else:
            print("salir")

if __name__ == "__main__":
    main()
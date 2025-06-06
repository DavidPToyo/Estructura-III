def estimacion_tiempo(pizza):
 
    cantidad_ingredientes = len(pizza.get("ingredientes", []))
    tiempo_estimado = 20 + (2 * cantidad_ingredientes)
    print(f"El tiempo estimado para que la pizza esté lista es de: {tiempo_estimado} minutos.")

agua = 500
azucar = 50
cafe = 5

min_agua = 200
min_azucar = 10
min_cafe = 1

def mostrar_menu_completo():
    print("\n--- MÁQUINA DE CAFÉ ---")
    print("1. Comprar un Café Espresso")
    print("2. Comprar un Capuccino")
    print("3. Comprar un Mocaccino")
    print("4. Gestión")
    print("5. Salir")

def mostrar_menu_limitado():
    print("\n--- MÁQUINA DE CAFÉ ---")
    print("1. Gestión")
    print("2. Salir")

productos = {
    "1": {"nombre": "Café Espresso", "agua": 30, "cafe": 1, "desc": "Café corto e intenso"},
    "2": {"nombre": "Café Capuccino", "agua": 60, "cafe": 1, "desc": "Café con espuma de leche cremosa y suave"},
    "3": {"nombre": "Café Mocaccino", "agua": 50, "cafe": 1, "desc": "Café con leche y chocolate, sabor dulce y cremoso"}
}

azucar_opciones = {
    "1": ("Nada", 0),
    "2": ("Poco", 5),
    "3": ("Medio", 10),
    "4": ("Bastante", 15),
    "5": ("Mucho", 20)
}

def gestion_recursos():
    global agua, azucar, cafe
    while True:
        print("\n--- GESTIÓN DE RECURSOS ---")
        print(f"Agua disponible: {agua} ml")
        print(f"Azúcar disponible: {azucar} g")
        print(f"Café disponible: {cafe} cartuchos")
        print("\nSeleccione un recurso para recargar:")
        print("1. Agua")
        print("2. Azúcar")
        print("3. Café")
        print("4. Volver al menú")

        eleccion = input("Opción [1,4]: ")
        match eleccion:
            case "1":
                try:
                    cantidad = int(input("¿Cuánta agua desea agregar (ml)?: "))
                    agua += cantidad
                    print("Agua recargada.")
                except ValueError:
                    print("Entrada inválida.")
            case "2":
                try:
                    cantidad = int(input("¿Cuánta azúcar desea agregar (g)?: "))
                    azucar += cantidad
                    print("Azúcar recargada.")
                except ValueError:
                    print("Entrada inválida.")
            case "3":
                try:
                    cantidad = int(input("¿Cuántos cartuchos de café desea agregar?: "))
                    cafe += cantidad
                    print("Café recargado.")
                except ValueError:
                    print("Entrada inválida.")
            case "4":
                break
            case _:
                print("Opción inválida.")

while True:
    recursos_ok = agua >= min_agua and azucar >= min_azucar and cafe >= min_cafe

    if recursos_ok:
        mostrar_menu_completo()
        opcion = input("Opción [1,5]: ")

        match opcion:
            case "1" | "2" | "3":
                print("\nOpciones de azúcar:")
                for k, (nombre, gramos) in azucar_opciones.items():
                    print(f"{k}. {nombre} ({gramos}g)")
                azucar_sel = input("Opción [1,5]: ")

                if azucar_sel not in azucar_opciones:
                    print("Selección inválida.")
                    continue

                azucar_g = azucar_opciones[azucar_sel][1]
                p = productos[opcion]

                if agua >= p["agua"] and azucar >= azucar_g and cafe >= p["cafe"]:
                    agua -= p["agua"]
                    azucar -= azucar_g
                    cafe -= p["cafe"]
                    print(f"\nPreparando {p['nombre']}...")
                    print(p["desc"])
                    print("¡Listo!\n")
                else:
                    print("No hay suficientes recursos para este producto.")

            case "4":
                gestion_recursos()

            case "5":
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida.")
    else:
        print("\n⚠ Recursos insuficientes. Solo se puede acceder a la gestión de recursos o salir.")
        mostrar_menu_limitado()
        opcion = input("Opción [1,2]: ")

        match opcion:
            case "1":
                gestion_recursos()
            case "2":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")

# Función para preparar el pollo a la plancha
def preparar_pollo_a_la_plancha(presentacion):
    if presentacion == "tiras":
        return "pollo a la plancha cortado en tiras"
    else:
        return "pollo a la plancha entero"

# Función para preparar salsa César con opción de pimienta negra
def preparar_salsa_cesar(pimienta_negra_molida):
    salsa = {
        "pimienta_negra": pimienta_negra_molida,
        "sal": "al gusto",
        "zumo_limon": "10 ml"
    }
    return salsa

# Función que devuelve un diccionario con toda la receta
def emplatado(nombre_receta, salsa, presentacion_pollo, ingredientes, pasos):
    return {
        "receta": nombre_receta,
        "salsa": salsa,
        "presentacion_pollo": presentacion_pollo,
        "ingredientes": ingredientes,
        "pasos": pasos
    }

# Receta 1: Ensalada César con pollo
def preparar_ensalada_cesar():
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(pimienta_negra_molida=True)

    ingredientes = ["lechuga romana", "pollo en tiras", "queso parmesano", "crutones", "salsa césar"]
    pasos = [
        "Lavar y cortar la lechuga",
        f"Agregar el {pollo}",
        "Incorporar el queso y los crutones",
        "Añadir la salsa césar"
    ]
    return emplatado("Ensalada César con Pollo", salsa, "tiras", ingredientes, pasos)

# Receta 2: Wrap de pollo con salsa César
def preparar_wrap_cesar():
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(pimienta_negra_molida=False)

    ingredientes = ["tortilla de trigo", "pollo en tiras", "lechuga", "salsa césar", "queso"]
    pasos = [
        "Calentar la tortilla",
        f"Agregar el {pollo}",
        "Añadir lechuga y queso",
        "Incorporar la salsa césar",
        "Enrollar el wrap"
    ]
    return emplatado("Wrap de Pollo con Salsa César", salsa, "tiras", ingredientes, pasos)

# Receta 3: Sándwich clásico de pollo
def preparar_sandwich_pollo():
    pollo = preparar_pollo_a_la_plancha("normal")
    salsa = preparar_salsa_cesar(pimienta_negra_molida=False)

    ingredientes = ["pan de sándwich", "queso", "lechuga", "tomate"]
    pasos = [
        "Tostar ligeramente el pan",
        f"Colocar el {pollo}",
        "Agregar el queso y vegetales",
        "Añadir la salsa"
    ]
    return emplatado("Sándwich Clásico de Pollo", salsa, "normal", ingredientes, pasos)

# Menú interactivo
def mostrar_menu():
    print("\n🍽️ ASISTENTE DE COCINA - MENÚ DE RECETAS 🍽️")
    print("1. Ensalada César con pollo")
    print("2. Wrap de pollo con salsa César")
    print("3. Sándwich clásico de pollo")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        receta = preparar_ensalada_cesar()
    elif opcion == "2":
        receta = preparar_wrap_cesar()
    elif opcion == "3":
        receta = preparar_sandwich_pollo()
    elif opcion == "4":
        print("Gracias por usar el asistente de cocina. ¡Buen provecho!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
        continue

    # Mostrar receta elegida
    print("\n📦 RECETA PREPARADA 📦")
    print("Nombre:", receta["receta"])
    print("Presentación del pollo:", receta["presentacion_pollo"])
    print("Salsa:", receta["salsa"])
    print("Ingredientes:")
    for ingrediente in receta["ingredientes"]:
        print(" -", ingrediente)
    print("Pasos:")
    for i, paso in enumerate(receta["pasos"], 1):
        print(f" {i}. {paso}")

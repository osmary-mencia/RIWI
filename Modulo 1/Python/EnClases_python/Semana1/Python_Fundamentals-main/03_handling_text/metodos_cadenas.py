# Imprime una línea decorativa
print("*" * 30)
print("|       Métodos de Texto en Python       |")
print("*" * 30)
print()

# 'in' verifica si una palabra está dentro de un texto
print("1. in: verifica si una palabra está dentro de un texto")
texto = "hola mundo cómo estás"
if "mundo" in texto:
    print("✅ La palabra 'mundo' está dentro del texto")
print()

# 'len()' cuenta la cantidad de caracteres (incluye espacios)
print("2. len: cuenta cuántos caracteres tiene un texto (incluye espacios)")
print("Texto:", texto)
print("Cantidad de caracteres:", len(texto))
print()

# 'upper()' convierte todo a MAYÚSCULAS
print("3. upper: convierte el texto a mayúsculas")
print(texto.upper())
print()

# 'lower()' convierte todo a minúsculas
print("4. lower: convierte el texto a minúsculas")
texto = "HOLA MUNDO"
print(texto.lower())
print()

# 'capitalize()' convierte la primera letra en mayúscula (las demás en minúscula)
print("5. capitalize: solo la primera letra del texto en mayúscula")
texto = "hola mundo"
print(texto.capitalize())
print()

# 'title()' pone la primera letra de cada palabra en mayúscula
print("6. title: primera letra de cada palabra en mayúscula")
print(texto.title())
print()

# 'count()' cuenta cuántas veces aparece una palabra o letra
print("7. count: cuántas veces aparece una palabra/letra en el texto")
texto = "anita lava la tina"
print("Cantidad de veces que aparece 'la':", texto.count("la"))
print()

# 'swapcase()' cambia mayúsculas a minúsculas y viceversa
print("8. swapcase: cambia mayúsculas por minúsculas y al revés")
texto = "HeLLo WoRLd"
print(texto.swapcase())
print()

# 'startswith()' verifica si el texto comienza con cierta palabra
print("9. startswith: ¿el texto empieza con cierta palabra?")
texto = "hola mundo"
print("¿Empieza con 'hola'?", texto.startswith("hola"))
print()

# 'endswith()' verifica si el texto termina con cierta palabra
print("10. endswith: ¿el texto termina con cierta palabra?")
print("¿Termina con 'mundo'?", texto.endswith("mundo"))
print()

# 'replace()' reemplaza un texto por otro
print("11. replace: reemplaza una palabra por otra")
print("Texto original:", texto)
print("Texto nuevo:", texto.replace("mundo", "familia"))
print()

# 'isdigit()' verifica si el texto contiene solo números
print("12. isdigit: ¿el texto es un número?")
numero = "12345"
palabra = "123abc"
print(f"¿'{numero}' es número?:", numero.isdigit())
print(f"¿'{palabra}' es número?:", palabra.isdigit())
print()

# 'strip()' elimina espacios al inicio y al final
print("13. strip: elimina espacios al principio y al final")
texto_con_espacios = "   Hola, mundo   "
print("Antes:", repr(texto_con_espacios))
print("Después:", repr(texto_con_espacios.strip()))
print()

#Solicitar la contraseña al usuario
contraseña = input("Crea una contraseña: ")

# Verificar los requisitos
if len(contraseña) < 8:
    print("Contraseña muy corta, tiene que tener al menos 8 caracteres.")
elif "@" not in contraseña:
    print("La contraseña debe incluir al menos un '@'.")
else:
    print("Contraseña válida.")

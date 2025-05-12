"""
🔸 Reto 2 – Combinado (for, while y if):
📌 Objetivo:
Usa un while para contar del 1 al 5.
En cada vuelta, usa un for para recorrer una lista de frutas: ["manzana", "banana", "uva"].
Solo imprime la fruta si el número del while es par.

🔍 Pista:

if numero % 2 == 0: para detectar si es par.

Puedes usar continue para saltar si no es par (opcional).
"""
numero = 1
lista_frutas = ["manzana", "banana", "uva"]

while numero <= 5:
    if numero % 2 == 0:
        print(f"Número {numero} es par. Mostrando frutas:")
        for fruta in lista_frutas:
            print(f"- {fruta}")
    else:
        print(f"Número {numero} es impar. No se muestran frutas.")
    
    numero += 1

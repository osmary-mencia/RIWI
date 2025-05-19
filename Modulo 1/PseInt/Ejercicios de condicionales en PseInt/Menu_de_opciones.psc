Algoritmo Menu_de_opciones
    Definir numero1, numero2, resultado Como Real
    Definir opcion_ Como Entero
    
    Escribir "ELIJA UNA OPCIÓN"
    Escribir "1. Sumar"
    Escribir "2. Restar"
    Escribir "3. Multiplicar"
    Escribir "4. Dividir"
    Leer opcion_
    
    Si opcion_ >= 1 Y opcion_ <= 4 Entonces
        Escribir "Ingrese el primer número:"
        Leer numero1
        Escribir "Ingrese el segundo número:"
        Leer numero2
        
        Segun opcion_ Hacer
            1:
                resultado <- numero1 + numero2
                Escribir "El resultado de la suma es: ", resultado
            2:
                resultado <- numero1 - numero2
                Escribir "El resultado de la resta es: ", resultado
            3:
                resultado <- numero1 * numero2
                Escribir "El resultado de la multiplicación es: ", resultado
            4:
                Si numero2 <> 0 Entonces
                    resultado <- numero1 / numero2
                    Escribir "El resultado de la división es: ", resultado
                Sino
                    Escribir "Error: No se puede dividir entre 0."
                FinSi
        FinSegun
    Sino
        Escribir "Opción inválida. Por favor, seleccione una opción del 1 al 4."
    FinSi
FinAlgoritmo


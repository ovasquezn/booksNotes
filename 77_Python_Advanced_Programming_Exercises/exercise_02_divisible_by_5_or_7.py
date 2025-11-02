"""
Exercise 02: Sum of numbers divisible by 5 or 7

Descripción:
All natural numbers divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15].
The sum of these numbers is: 51. In this exercise, we treat zero as a natural number.

Find the sum of all numbers that are divisible by 5 or 7 less than 100.

Requisitos:
- Present the solution in the form of a function called calculate()
- Call calculate() function and print the result to the console
- Treat zero as a natural number

Ejemplo:
Para números menores que 20: [0, 5, 7, 10, 14, 15] → suma = 51
Para números menores que 100: [calcular] → suma = ?
"""

# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate():
    """
    Calcula la suma de todos los números naturales (incluyendo 0) que son
    divisibles por 5 o 7 y son menores que 100.
    
    Returns:
        int: La suma de todos los números que cumplen la condición
    """
    # Generar todos los números menores que 100 que son divisibles por 5 o 7
    numbers = [num for num in range(100) if num % 5 == 0 or num % 7 == 0]
    return sum(numbers)


def calculate_alternative():
    """
    Versión alternativa usando set para evitar duplicados (aunque en este caso
    no hay números divisibles por ambos, es una buena práctica).
    
    Returns:
        int: La suma de todos los números que cumplen la condición
    """
    # Usar set para evitar duplicados (números divisibles por ambos 5 y 7)
    numbers = set()
    
    # Agregar números divisibles por 5
    for num in range(0, 100, 5):
        numbers.add(num)
    
    # Agregar números divisibles por 7
    for num in range(0, 100, 7):
        numbers.add(num)
    
    return sum(numbers)

# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book():
    """
    Solución propuesta en el libro.
    """
    numbers = []
    for i in range(100):
        if i%5 ==0 or i%7==0:
            numbers.append(i)
    total = sum(numbers)
    return total

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 02: Sum of numbers divisible by 5 or 7")
    print("=" * 60)
    
    # Verificar ejemplo del problema (menores que 20)
    print("\nVerificación con ejemplo (números < 20):")
    example_numbers = [num for num in range(20) if num % 5 == 0 or num % 7 == 0]
    example_sum = sum(example_numbers)
    print(f"  Números encontrados: {example_numbers}")
    print(f"  Suma esperada: 51")
    print(f"  Suma calculada: {example_sum}")
    print(f"  ✓ Correcto" if example_sum == 51 else f"  ✗ Incorrecto")
    
    # Solución propia - números menores que 100
    print("\nSolución propia (números < 100):")
    result = calculate()
    print(f"  Resultado: {result}")
    
    # Verificar con solución alternativa
    print("\nSolución alternativa (usando set):")
    result_alt = calculate_alternative()
    print(f"  Resultado: {result_alt}")
    print(f"  ✓ Ambos métodos coinciden" if result == result_alt else "  ✗ Diferencia detectada")
    
    # Solución del libro (cuando esté disponible)
    print("\nSolución del libro:")
    book_result = calculate_book()
    print(f"  Resultado: {book_result}")
    
    # Mostrar los números encontrados para verificación
    print("\nPrimeros y últimos números encontrados:")
    all_numbers = [num for num in range(100) if num % 5 == 0 or num % 7 == 0]
    print(f"  Total de números: {len(all_numbers)}")
    print(f"  Primeros 10: {all_numbers[:10]}")
    print(f"  Últimos 10: {all_numbers[-10:]}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Como requiere el problema: llamar calculate() y imprimir el resultado
    print(calculate())
    
    # También ejecutar las pruebas detalladas
    main()


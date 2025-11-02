"""
Exercise 03: Sum of even Fibonacci numbers

Descripción:
Consider the Fibonacci sequence. It is a sequence of natural numbers defined 
recursively as follows:
• the first element of the sequence is 0
• the second element of the sequence is 1
• each next element of the sequence is the sum of the previous two elements

The beginning of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all even elements of the Fibonacci sequence with values less than 
1,000,000 (1 million).

Requisitos:
- Present the solution in the form of a function called calculate()
- Call calculate() function and print the result to the console
- Only consider Fibonacci numbers less than 1,000,000

Ejemplo:
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
Even Fibonacci numbers < 100: [0, 2, 8, 34] → suma = 44
Even Fibonacci numbers < 1,000,000: [calcular] → suma = ?
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate():
    """
    Calcula la suma de todos los números pares de la secuencia de Fibonacci
    que son menores que 1,000,000.
    
    Returns:
        int: La suma de todos los números pares de Fibonacci menores que 1,000,000
    """
    # Inicializar los dos primeros términos
    a, b = 0, 1
    even_sum = 0
    
    # Generar la secuencia hasta llegar a 1,000,000
    while a < 1_000_000:
        # Si el número actual es par, agregarlo a la suma
        if a % 2 == 0:
            even_sum += a
        
        # Calcular el siguiente término de Fibonacci
        a, b = b, a + b
    
    return even_sum


def calculate_alternative():
    """
    Versión alternativa que genera todos los Fibonacci y luego filtra los pares.
    
    Returns:
        int: La suma de todos los números pares de Fibonacci menores que 1,000,000
    """
    # Generar todos los números de Fibonacci menores que 1,000,000
    fibonacci_sequence = [0, 1]
    
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fib >= 1_000_000:
            break
        fibonacci_sequence.append(next_fib)
    
    # Filtrar solo los números pares y sumarlos
    even_fibonacci = [num for num in fibonacci_sequence if num % 2 == 0]
    return sum(even_fibonacci)


def calculate_generator():
    """
    Versión usando generador de Fibonacci (más eficiente en memoria).
    
    Returns:
        int: La suma de todos los números pares de Fibonacci menores que 1,000,000
    """
    def fibonacci_generator():
        """Generador que produce números de Fibonacci."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    even_sum = 0
    fib_gen = fibonacci_generator()
    
    for fib_num in fib_gen:
        if fib_num >= 1_000_000:
            break
        if fib_num % 2 == 0:
            even_sum += fib_num
    
    return even_sum


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book():
    """
    Solución propuesta en el libro.
    (Agregar la solución del libro aquí cuando esté disponible)
    """
    total = 0
    a = 0
    b = 1
    while a < 1_000_000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total 


# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 03: Sum of even Fibonacci numbers")
    print("=" * 60)
    
    # Verificar ejemplo del problema (pares menores que 100)
    print("\nVerificación con ejemplo (números pares < 100):")
    fib_sequence_small = []
    a, b = 0, 1
    while a < 100:
        fib_sequence_small.append(a)
        a, b = b, a + b
    
    even_fib_small = [num for num in fib_sequence_small if num % 2 == 0]
    example_sum = sum(even_fib_small)
    print(f"  Secuencia Fibonacci < 100: {fib_sequence_small}")
    print(f"  Números pares: {even_fib_small}")
    print(f"  Suma esperada: 44 (0 + 2 + 8 + 34)")
    print(f"  Suma calculada: {example_sum}")
    print(f"  ✓ Correcto" if example_sum == 44 else f"  ✗ Incorrecto")
    
    # Solución propia - números pares menores que 1,000,000
    print("\nSolución propia (pares < 1,000,000):")
    result = calculate()
    print(f"  Resultado: {result:,}")
    
    # Verificar con solución alternativa
    print("\nSolución alternativa (usando lista):")
    result_alt = calculate_alternative()
    print(f"  Resultado: {result_alt:,}")
    print(f"  ✓ Ambos métodos coinciden" if result == result_alt else "  ✗ Diferencia detectada")
    
    # Verificar con solución usando generador
    print("\nSolución con generador:")
    result_gen = calculate_generator()
    print(f"  Resultado: {result_gen:,}")
    print(f"  ✓ Todos los métodos coinciden" if result == result_gen else "  ✗ Diferencia detectada")
    
    # Solución del libro (cuando esté disponible)
    print("\nSolución del libro:")
    book_result = calculate_book()
    print(f"  Resultado: {book_result:,}")

    # Mostrar algunos números pares encontrados para verificación
    print("\nAnálisis de la secuencia:")
    fib_list = []
    a, b = 0, 1
    while a < 1_000_000:
        fib_list.append(a)
        a, b = b, a + b
    
    even_fib_list = [num for num in fib_list if num % 2 == 0]
    print(f"  Total de números Fibonacci < 1,000,000: {len(fib_list)}")
    print(f"  Total de números pares: {len(even_fib_list)}")
    print(f"  Primeros 5 pares: {even_fib_list[:5]}")
    print(f"  Últimos 5 pares: {even_fib_list[-5:]}")
    
    # Observación interesante: cada tercer número de Fibonacci es par
    print("\nObservación:")
    print("  En la secuencia de Fibonacci, cada tercer número es par:")
    pattern_check = []
    a, b = 0, 1
    for i in range(12):
        pattern_check.append((i, a, "par" if a % 2 == 0 else "impar"))
        a, b = b, a + b
    for idx, val, parity in pattern_check[:12]:
        print(f"    F({idx}) = {val:3d} ({parity})")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Como requiere el problema: llamar calculate() y imprimir el resultado
    print(calculate())
    
    # También ejecutar las pruebas detalladas
    main()


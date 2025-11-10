"""
Exercise 05: Greatest Prime Factor

Descripción:
In number theory, integer factorization is the decomposition of a composite number 
into a product of smaller integers. If these factors are further restricted to 
prime numbers, the process is called prime factorization.

Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ... 
Reminder: The number 1 is not a prime number.

A number that is greater than 1 and is not a prime is called a composite number.

Examples of composite numbers: 4, 6, 8, 9, 10, 12, 14, 15, 16, ...

We can break down a composite number into prime factors. For example:
• 15 = 3 * 5
• 36 = 2 * 2 * 3 * 3

The largest prime factor for 15 is 5, and for 36 is 3.

Using the previous exercise, implement a function that takes a natural number as 
an argument and returns the greatest prime factor of that number.

Requisitos:
- Implement a function that takes a natural number as an argument
- Returns the greatest prime factor of that number
- Present the solution in the form of a function called calculate()

Ejemplo:
[IN]: calculate(13195)
[OUT]: 29

[IN]: calculate(15)
[OUT]: 5

[IN]: calculate(36)
[OUT]: 3
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

from math import factorial


def calculate(n):
    """
    Encuentra el mayor factor primo de un número natural.
    
    Args:
        n (int): Número natural
        
    Returns:
        int: El mayor factor primo del número
        
    Examples:
        >>> calculate(13195)
        29
        >>> calculate(15)
        5
        >>> calculate(36)
        3
    """
    if n < 2:
        return None  # Los números menores que 2 no tienen factores primos
    
    # El mayor factor primo será el último factor que encontremos
    # o el número mismo si es primo
    num = n
    largest_factor = 1
    
    # Dividir por 2 mientras sea posible
    while num % 2 == 0:
        largest_factor = 2
        num //= 2
    
    # Probar números impares desde 3 hasta sqrt(num)
    i = 3
    while i * i <= num:
        while num % i == 0:
            largest_factor = i
            num //= i
        i += 2
    
    # Si num > 1, entonces es el último (y mayor) factor primo
    if num > 1:
        largest_factor = num
    
    return largest_factor


def calculate_using_factorization(n):
    """
    Versión que usa la factorización completa y luego toma el máximo.
    Menos eficiente pero más directa.
    
    Args:
        n (int): Número natural
        
    Returns:
        int: El mayor factor primo del número
    """
    if n < 2:
        return None
    
    factors = []
    num = n
    
    # Factorización completa
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    
    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 2
    
    if num > 1:
        factors.append(num)
    
    return max(factors) if factors else None


def calculate_optimized(n):
    """
    Versión optimizada que encuentra directamente el mayor factor primo
    sin necesidad de almacenar todos los factores.
    
    Args:
        n (int): Número natural
        
    Returns:
        int: El mayor factor primo del número
    """
    if n < 2:
        return None
    
    num = n
    largest_factor = 1
    
    # Dividir por 2 mientras sea posible
    while num % 2 == 0:
        largest_factor = 2
        num //= 2
    
    # Probar números impares desde 3
    i = 3
    while i * i <= num:
        if num % i == 0:
            largest_factor = i
            num //= i
        else:
            i += 2
    
    # El último factor (si existe) es el mayor
    if num > 1:
        largest_factor = num
    
    return largest_factor


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book(n):
    """
    Solución propuesta en el libro.
    """
    i = 2
    factors = []
    while i*i <= n:
        if not n%i == 0:
            i += 1
        else:
            n = n // i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return max(factors)

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 05: Greatest Prime Factor")
    print("=" * 60)
    
    # Casos de prueba del problema
    test_cases = [
        (13195, 29),
        (15, 5),
        (36, 3),
        (2, 2),  # Número primo
        (3, 3),  # Número primo
        (4, 2),
        (6, 3),
        (12, 3),
        (100, 5),
        (17, 17),  # Número primo
        (48, 3),
        (97, 97),  # Número primo
    ]
    
    print("\nCasos de prueba:")
    all_passed = True
    
    for number, expected in test_cases:
        result = calculate(number)
        is_correct = result == expected
        all_passed = all_passed and is_correct
        
        status = "✓" if is_correct else "✗"
        print(f"\n  {status} calculate({number})")
        print(f"    Esperado: {expected}")
        print(f"    Obtenido: {result}")
        if not is_correct:
            print(f"    ERROR")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("Todos los casos de prueba pasaron")
    else:
        print("Algunos casos de prueba fallaron")
    print("=" * 60)
    
    # Verificar que todas las versiones dan el mismo resultado
    print("\nVerificación de consistencia entre métodos:")
    test_numbers = [13195, 15, 36, 100, 2310, 97]
    
    for num in test_numbers:
        result1 = calculate(num)
        result2 = calculate_using_factorization(num)
        result3 = calculate_optimized(num)
        
        all_match = result1 == result2 == result3
        
        print(f"\n  Número: {num}")
        print(f"    Método 1 (directo):           {result1}")
        print(f"    Método 2 (factorización):     {result2}")
        print(f"    Método 3 (optimizado):       {result3}")
        print(f"    {'✓ Todos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Verificar con factorización: el mayor factor debe estar en los factores
    print("\nVerificación matemática:")
    print("  (El mayor factor primo debe estar en la factorización)")
    for num in [13195, 15, 36, 100, 2310]:
        greatest = calculate(num)
        # Obtener factores únicos
        factors = []
        temp = num
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                factors.append(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            factors.append(temp)
        
        is_in_factors = greatest in factors
        print(f"  {num}: mayor factor = {greatest}, factores únicos = {factors} {'✓' if is_in_factors else '✗'}")
    
    # Solución del libro
    print("\nSolución del libro:")
    book_result = calculate_book(13195)
    print(f"  calculate_book(13195) = {book_result}")
    print(f"  {'✓ Coincide' if book_result == 29 else '✗ Diferencia'}")

if __name__ == "__main__":
    # Ejecutar las pruebas
    main()
    
    # Ejemplos adicionales interactivos
    print("\n" + "=" * 60)
    print("Ejemplos adicionales:")
    print("=" * 60)
    
    examples = [13195, 100, 2310, 97, 600851475143]
    for num in examples:
        result = calculate(num)
        print(f"calculate({num}) = {result}")


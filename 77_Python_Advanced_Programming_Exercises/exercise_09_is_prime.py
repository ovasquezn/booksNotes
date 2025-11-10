"""
Exercise 09: Prime Number Check

Descripción:
A prime number is a natural number greater than 1 that is not a product of two 
smaller natural numbers.

Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...

Requisitos:
- Implement a function called is_prime() that takes a natural number as an argument
- Checks if it is a prime number
- Returns True if it is a prime number, otherwise False

Ejemplo:
[IN]: is_prime(11)
[OUT]: True

[IN]: is_prime(4)
[OUT]: False

[IN]: is_prime(2)
[OUT]: True
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def is_prime(n):
    """
    Verifica si un número natural es primo.
    
    Un número primo es un número natural mayor que 1 que no es producto de 
    dos números naturales menores.
    
    Args:
        n (int): Número natural a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
        
    Examples:
        >>> is_prime(11)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
    """
    # Los números menores que 2 no son primos
    if n < 2:
        return False
    
    # 2 es el único número primo par
    if n == 2:
        return True
    
    # Los números pares mayores que 2 no son primos
    if n % 2 == 0:
        return False
    
    # Verificar divisibilidad solo con números impares desde 3 hasta sqrt(n)
    # Si n tiene un divisor mayor que sqrt(n), también tiene uno menor
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Solo probar números impares
    
    return True


def is_prime_optimized(n):
    """
    Versión optimizada: verifica divisibilidad solo hasta sqrt(n) y solo con 
    números impares después de verificar 2.
    
    Args:
        n (int): Número natural a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if n < 2:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Verificar divisibilidad con números de la forma 6k ± 1
    # Todos los primos mayores que 3 son de esta forma
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def is_prime_simple(n):
    """
    Versión simple y directa: verifica todos los divisores desde 2 hasta n-1.
    Menos eficiente pero más fácil de entender.
    
    Args:
        n (int): Número natural a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def is_prime_sqrt(n):
    """
    Versión que verifica divisores hasta sqrt(n) (más eficiente que la simple).
    
    Args:
        n (int): Número natural a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    # Verificar divisibilidad desde 2 hasta sqrt(n)
    import math
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def is_prime_book(n):
    """
    Solución propuesta en el libro.
    """
    if n<2:
        return False
    if n%2 == 0:
        return n==2
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 09: Prime Number Check")
    print("=" * 60)
    
    # Casos de prueba
    test_cases = [
        (11, True),
        (4, False),
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (13, True),
        (17, True),
        (19, True),
        (1, False),
        (0, False),
        (6, False),
        (8, False),
        (9, False),
        (10, False),
        (12, False),
        (15, False),
        (20, False),
        (23, True),
        (29, True),
        (31, True),
        (37, True),
        (41, True),
        (43, True),
        (47, True),
        (97, True),
        (100, False),
    ]
    
    print("\nCasos de prueba:")
    all_passed = True
    
    for number, expected in test_cases:
        result = is_prime(number)
        is_correct = result == expected
        all_passed = all_passed and is_correct
        
        status = "✓" if is_correct else "✗"
        prime_str = "primo" if expected else "no primo"
        print(f"\n  {status} is_prime({number})")
        print(f"    Esperado: {expected} ({prime_str})")
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
    test_numbers = [2, 3, 4, 5, 7, 11, 13, 17, 19, 20, 23, 29, 31, 37, 97, 100]
    
    for num in test_numbers:
        result1 = is_prime(num)
        result2 = is_prime_optimized(num)
        result3 = is_prime_simple(num)
        result4 = is_prime_sqrt(num)
        
        all_match = result1 == result2 == result3 == result4
        
        print(f"\n  is_prime({num}):")
        print(f"    Método 1 (optimizado):  {result1}")
        print(f"    Método 2 (6k±1):        {result2}")
        print(f"    Método 3 (simple):      {result3}")
        print(f"    Método 4 (sqrt):        {result4}")
        print(f"    {'✓ Todos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Lista de primos conocidos
    print("\nPrimeros números primos (verificación):")
    known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(f"  Verificando los primeros 25 números primos:")
    all_are_primes = all(is_prime(p) for p in known_primes)
    print(f"  {'✓ Todos son identificados como primos' if all_are_primes else '✗ Error en la verificación'}")
    
    # Verificar que números compuestos no son identificados como primos
    print("\nNúmeros compuestos (verificación):")
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
    all_are_composites = all(not is_prime(c) for c in composites)
    print(f"  Verificando números compuestos:")
    print(f"  {'✓ Ninguno es identificado como primo' if all_are_composites else '✗ Error en la verificación'}")
    
    # Análisis de eficiencia
    print("\nAnálisis:")
    print("  Números primos menores que 100:")
    primes_under_100 = [n for n in range(2, 100) if is_prime(n)]
    print(f"    Total: {len(primes_under_100)} números primos")
    print(f"    Lista: {primes_under_100}")
    
    # Solución del libro
    print("\nSolución del libro:")
    book_result = is_prime_book(11)
    print(f"  is_prime_book(11) = {book_result}")
    print(f"  {'✓ Coincide' if book_result == True else '✗ Diferencia'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Ejecutar las pruebas
    main()
    
    # Ejemplos adicionales interactivos
    print("\n" + "=" * 60)
    print("Ejemplos adicionales:")
    print("=" * 60)
    
    examples = [2, 3, 4, 11, 17, 20, 23, 29, 97, 100]
    for num in examples:
        result = is_prime(num)
        status = "primo" if result else "no primo"
        print(f"is_prime({num}) = {result} ({status})")


"""
Exercise 04: Prime Factorization

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
• 48 = 2 * 2 * 2 * 2 * 3

Requisitos:
- Implement a function that takes a natural number as an argument
- Returns a list containing the prime factorization of that number
- Present the solution in the form of a function called calculate()

Ejemplo:
[IN]: calculate(48)
[OUT]: [2, 2, 2, 2, 3]

[IN]: calculate(15)
[OUT]: [3, 5]

[IN]: calculate(36)
[OUT]: [2, 2, 3, 3]
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate(n):
    """
    Calcula la factorización en números primos de un número natural.
    
    Args:
        n (int): Número natural a factorizar
        
    Returns:
        list: Lista de factores primos (puede incluir duplicados)
        
    Examples:
        >>> calculate(48)
        [2, 2, 2, 2, 3]
        >>> calculate(15)
        [3, 5]
        >>> calculate(36)
        [2, 2, 3, 3]
    """
    if n < 2:
        return []  # Los números menores que 2 no tienen factorización prima
    
    factors = []
    num = n
    
    # Dividir por 2 mientras sea posible
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    
    # Probar números impares desde 3 hasta sqrt(num)
    # Los factores primos después de 2 son impares
    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 2
    
    # Si num > 1, entonces es un factor primo
    if num > 1:
        factors.append(num)
    
    return factors


def calculate_alternative(n):
    """
    Versión alternativa usando un enfoque más simple e intuitivo.
    
    Args:
        n (int): Número natural a factorizar
        
    Returns:
        list: Lista de factores primos
    """
    if n < 2:
        return []
    
    factors = []
    num = n
    
    # Probar todos los números desde 2 hasta num
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    
    # Si queda algo, es el último factor primo
    if num > 1:
        factors.append(num)
    
    return factors


def calculate_recursive(n, divisor=2):
    """
    Versión recursiva de la factorización (menos eficiente pero educativa).
    
    Args:
        n (int): Número natural a factorizar
        divisor (int): Divisor actual (inicia en 2)
        
    Returns:
        list: Lista de factores primos
    """
    if n < 2:
        return []
    
    if n == 2:
        return [2]
    
    if divisor * divisor > n:
        return [n] if n > 1 else []
    
    if n % divisor == 0:
        return [divisor] + calculate_recursive(n // divisor, divisor)
    else:
        return calculate_recursive(n, divisor + 1)


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book(n):
    """
    Solución propuesta en el libro.
    (Agregar la solución del libro aquí cuando esté disponible)
    """
    i = 2
    factors = []
    while i*i <= n:
        if not n % i == 0:
            i+=1
        else:
            n = n//i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 04: Prime Factorization")
    print("=" * 60)
    
    # Casos de prueba del problema
    test_cases = [
        (48, [2, 2, 2, 2, 3]),
        (15, [3, 5]),
        (36, [2, 2, 3, 3]),
        (2, [2]),  # Número primo
        (3, [3]),  # Número primo
        (4, [2, 2]),
        (6, [2, 3]),
        (12, [2, 2, 3]),
        (100, [2, 2, 5, 5]),
        (17, [17]),  # Número primo
        (1, []),  # Caso especial
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
            print(f"ERROR")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("Todos los casos de prueba pasaron")
    else:
        print("Algunos casos de prueba fallaron")
    print("=" * 60)
    
    # Verificar que todas las versiones dan el mismo resultado
    print("\nVerificación de consistencia entre métodos:")
    test_numbers = [48, 15, 36, 100, 2310]
    
    for num in test_numbers:
        result1 = calculate(num)
        result2 = calculate_alternative(num)
        result3 = calculate_recursive(num)
        
        all_match = result1 == result2 == result3
        
        print(f"\n  Número: {num}")
        print(f"    Método 1 (optimizado):  {result1}")
        print(f"    Método 2 (alternativo): {result2}")
        print(f"    Método 3 (recursivo):   {result3}")
        print(f"    {'✓ Todos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Verificar factorización: el producto debe ser igual al número original
    print("\nVerificación matemática (producto de factores = número original):")
    for num in [48, 15, 36, 100, 2310, 97]:
        factors = calculate(num)
        if factors:
            product = 1
            for factor in factors:
                product *= factor
            match = product == num
            print(f"  {num}: {factors} → producto = {product} {'✓' if match else '✗'}")
        else:
            print(f"  {num}: [] (número menor que 2)")
    
    # Solución del libro
    print("\nSolución del libro:")
        # Probar con un caso de ejemplo
    book_result = calculate_book(48)
    print(f"  calculate_book(48) = {book_result}")
    print(f"  {'✓ Coincide' if book_result == [2, 2, 2, 2, 3] else '✗ Diferencia'}")

if __name__ == "__main__":
    # Ejecutar las pruebas
    main()
    
    # Ejemplos adicionales interactivos
    print("\n" + "=" * 60)
    print("Ejemplos adicionales:")
    print("=" * 60)
    
    examples = [48, 100, 2310, 97]
    for num in examples:
        result = calculate(num)
        print(f"calculate({num}) = {result}")


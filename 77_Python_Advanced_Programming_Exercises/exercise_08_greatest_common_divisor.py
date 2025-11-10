"""
Exercise 08: Greatest Common Divisor (GCD)

Descripción:
Greatest Common Divisor (GCD) of two integers - this is the largest natural number 
that divides both of these numbers without a remainder.

For example, for numbers 32 and 48, the greatest common divisor is 16, which we 
can write GCD(32, 48) = 16.

Requisitos:
- Implement a function called greatest_common_divisor() that determines the 
  greatest common divisor of two numbers

Ejemplo:
[IN]: greatest_common_divisor(32, 48)
[OUT]: 16

[IN]: greatest_common_divisor(48, 18)
[OUT]: 6

[IN]: greatest_common_divisor(17, 13)
[OUT]: 1
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def greatest_common_divisor(a, b):
    """
    Calcula el máximo común divisor (GCD) de dos números enteros usando el 
    algoritmo de Euclides.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor de a y b
        
    Examples:
        >>> greatest_common_divisor(32, 48)
        16
        >>> greatest_common_divisor(48, 18)
        6
        >>> greatest_common_divisor(17, 13)
        1
    """
    # Manejar casos especiales
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    
    # Algoritmo de Euclides
    # GCD(a, b) = GCD(b, a mod b) hasta que b == 0
    a, b = abs(a), abs(b)  # Trabajar con valores absolutos
    
    while b != 0:
        a, b = b, a % b
    
    return a


def greatest_common_divisor_iterative(a, b):
    """
    Versión iterativa más explícita del algoritmo de Euclides.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor de a y b
    """
    a, b = abs(a), abs(b)
    
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Asegurar que a >= b
    if a < b:
        a, b = b, a
    
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    
    return a


def greatest_common_divisor_recursive(a, b):
    """
    Versión recursiva del algoritmo de Euclides.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor de a y b
    """
    a, b = abs(a), abs(b)
    
    if b == 0:
        return a
    
    return greatest_common_divisor_recursive(b, a % b)


def greatest_common_divisor_naive(a, b):
    """
    Versión naive: probar todos los números desde el menor hasta 1.
    Menos eficiente pero más fácil de entender.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor de a y b
    """
    a, b = abs(a), abs(b)
    
    if a == 0 or b == 0:
        return max(a, b)
    
    # Empezar desde el menor de los dos números
    start = min(a, b)
    
    # Probar desde start hacia abajo hasta encontrar un divisor común
    for i in range(start, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    
    return 1


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def greatest_common_divisor_book(a, b):
    """
    Solución propuesta en el libro.
    """
    while b:
        a,b = b,a%b
    return a

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 08: Greatest Common Divisor (GCD)")
    print("=" * 60)
    
    # Casos de prueba
    test_cases = [
        (32, 48, 16),
        (48, 18, 6),
        (17, 13, 1),
        (100, 25, 25),
        (56, 42, 14),
        (81, 27, 27),
        (0, 5, 5),
        (5, 0, 5),
        (7, 7, 7),
        (100, 1, 1),
        (-32, 48, 16),  # Con números negativos
        (32, -48, 16),
    ]
    
    print("\nCasos de prueba:")
    all_passed = True
    
    for a, b, expected in test_cases:
        result = greatest_common_divisor(a, b)
        is_correct = result == expected
        all_passed = all_passed and is_correct
        
        status = "✓" if is_correct else "✗"
        print(f"\n  {status} greatest_common_divisor({a}, {b})")
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
    test_pairs = [(32, 48), (48, 18), (100, 25), (56, 42), (17, 13)]
    
    for a, b in test_pairs:
        result1 = greatest_common_divisor(a, b)
        result2 = greatest_common_divisor_iterative(a, b)
        result3 = greatest_common_divisor_recursive(a, b)
        result4 = greatest_common_divisor_naive(a, b)
        
        all_match = result1 == result2 == result3 == result4
        
        print(f"\n  GCD({a}, {b}):")
        print(f"    Método 1 (Euclides):     {result1}")
        print(f"    Método 2 (iterativo):    {result2}")
        print(f"    Método 3 (recursivo):    {result3}")
        print(f"    Método 4 (naive):        {result4}")
        print(f"    {'✓ Todos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Verificación matemática: el GCD debe dividir a ambos números
    print("\nVerificación matemática (GCD divide a ambos números):")
    for a, b in [(32, 48), (48, 18), (100, 25), (56, 42)]:
        gcd = greatest_common_divisor(a, b)
        divides_a = a % gcd == 0
        divides_b = b % gcd == 0
        print(f"  GCD({a}, {b}) = {gcd}")
        print(f"    {a} % {gcd} = {a % gcd} {'✓' if divides_a else '✗'}")
        print(f"    {b} % {gcd} = {b % gcd} {'✓' if divides_b else '✗'}")
    
    # Propiedades del GCD
    print("\nPropiedades del GCD:")
    a, b = 32, 48
    gcd_ab = greatest_common_divisor(a, b)
    gcd_ba = greatest_common_divisor(b, a)
    print(f"  GCD({a}, {b}) = GCD({b}, {a}): {gcd_ab} = {gcd_ba} {'✓' if gcd_ab == gcd_ba else '✗'}")
    
    # GCD de múltiplos
    a, b = 6, 9
    gcd_ab = greatest_common_divisor(a, b)
    print(f"  GCD({a}, {b}) = {gcd_ab}")
    print(f"  GCD({a*2}, {b*2}) = {greatest_common_divisor(a*2, b*2)} = {gcd_ab * 2} {'✓' if greatest_common_divisor(a*2, b*2) == gcd_ab * 2 else '✗'}")
    
    # Solución del libro
    print("\nSolución del libro:")
    book_result = greatest_common_divisor_book(32, 48)
    print(f"  greatest_common_divisor_book(32, 48) = {book_result}")
    print(f"  {'✓ Coincide' if book_result == 16 else '✗ Diferencia'}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Ejecutar las pruebas
    main()
    
    # Ejemplos adicionales interactivos
    print("\n" + "=" * 60)
    print("Ejemplos adicionales:")
    print("=" * 60)
    
    examples = [(32, 48), (48, 18), (100, 25), (56, 42), (17, 13)]
    for a, b in examples:
        result = greatest_common_divisor(a, b)
        print(f"greatest_common_divisor({a}, {b}) = {result}")


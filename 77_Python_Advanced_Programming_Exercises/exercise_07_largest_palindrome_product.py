"""
Exercise 07: Largest Palindromic Number from Two-digit Product

Descripción:
Consider the palindromic numbers. A palindromic or symmetric number is a number that 
does not change when you write its digits in reverse order.

Some examples of palindromic numbers:
• 363
• 2882
• 29492

Implement a function that returns the largest palindromic number resulting from the 
product of two-digit numbers.

Requisitos:
- Implement a function that returns the largest palindromic number from the product 
  of two-digit numbers
- Present the solution in the form of a function called calculate()
- Call calculate() function and print the result to the console

Ejemplo:
Expected result: 9009

Two-digit numbers range: 10 to 99
Largest palindrome product: 9009 (91 × 99 = 9009)
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate():
    """
    Encuentra el mayor número palindrómico que resulta del producto de dos 
    números de 2 dígitos.
    
    Returns:
        int: El mayor número palindrómico producto de dos números de 2 dígitos
    """
    largest_palindrome = 0
    
    # Generar todos los productos de números de 2 dígitos (10-99)
    for i in range(10, 100):
        for j in range(10, 100):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    
    return largest_palindrome


def calculate_optimized():
    """
    Versión optimizada: empezar desde los números más grandes y parar cuando
    encontremos un palindrómico que no pueda ser superado.
    
    Returns:
        int: El mayor número palindrómico producto de dos números de 2 dígitos
    """
    largest_palindrome = 0
    
    # Empezar desde los números más grandes hacia abajo
    for i in range(99, 9, -1):
        for j in range(99, 9, -1):
            product = i * j
            # Si el producto es menor que el mayor palindrómico encontrado,
            # no necesitamos seguir con este i
            if product < largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product
    
    return largest_palindrome


def calculate_with_factors():
    """
    Versión que también retorna los factores que producen el mayor palindrómico.
    
    Returns:
        tuple: (mayor_palindrómico, factor1, factor2)
    """
    largest_palindrome = 0
    factors = (0, 0)
    
    for i in range(10, 100):
        for j in range(10, 100):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                factors = (i, j)
    
    return (largest_palindrome, factors[0], factors[1])


def is_palindrome(n):
    """
    Verifica si un número es palindrómico.
    
    Args:
        n (int): Número a verificar
        
    Returns:
        bool: True si el número es palindrómico, False en caso contrario
    """
    num_str = str(n)
    return num_str == num_str[::-1]


def is_palindrome_numeric(n):
    """
    Verifica si un número es palindrómico sin convertir a string.
    
    Args:
        n (int): Número a verificar
        
    Returns:
        bool: True si el número es palindrómico, False en caso contrario
    """
    if n < 10:
        return True
    
    original = n
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    
    return original == reversed_num


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book():
    """
    Solución propuesta en el libro.
    """
    numbers = []
    for i in range(10,100):
        for j in range(10, 100):
            if str(i*j) == str(i*j)[::-1]:
                numbers.append(i*j)
    return max(numbers)


# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 07: Largest Palindromic Number from Two-digit Product")
    print("=" * 60)
    
    # Resultado esperado
    expected = 9009
    
    print("\nResultado esperado: 9009")
    print("\nVerificación de métodos:")
    
    # Método 1: Búsqueda completa
    result1 = calculate()
    print(f"\n  Método 1 (búsqueda completa): {result1}")
    print(f"    {'✓ Correcto' if result1 == expected else '✗ Incorrecto'}")
    
    # Método 2: Optimizado
    result2 = calculate_optimized()
    print(f"\n  Método 2 (optimizado): {result2}")
    print(f"    {'✓ Correcto' if result2 == expected else '✗ Incorrecto'}")
    
    # Método 3: Con factores
    result3, factor1, factor2 = calculate_with_factors()
    print(f"\n  Método 3 (con factores): {result3}")
    print(f"    Factores: {factor1} × {factor2} = {result3}")
    print(f"    {'✓ Correcto' if result3 == expected else '✗ Incorrecto'}")
    
    # Verificar consistencia
    all_match = result1 == result2 == result3 == expected
    print(f"\n  {'✓ Todos los métodos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Verificar que 9009 es realmente 91 × 99
    print("\nVerificación matemática:")
    print(f"  91 × 99 = {91 * 99}")
    print(f"  ¿Es palindrómico? {is_palindrome(91 * 99)}")
    print(f"  {'✓ Confirmado' if 91 * 99 == expected and is_palindrome(91 * 99) else '✗ Error'}")
    
    # Encontrar todos los palindrómicos y sus factores
    print("\nTodos los palindrómicos y sus factores:")
    palindromes = []
    for i in range(10, 100):
        for j in range(i, 100):  # j >= i para evitar duplicados
            product = i * j
            if is_palindrome(product):
                palindromes.append((product, i, j))
    
    # Ordenar por producto descendente
    palindromes.sort(reverse=True, key=lambda x: x[0])
    
    print(f"  Total de palindrómicos encontrados: {len(palindromes)}")
    print(f"  Top 10 palindrómicos:")
    for idx, (prod, f1, f2) in enumerate(palindromes[:10], 1):
        print(f"    {idx}. {prod} = {f1} × {f2}")
    
    # Verificar que el mayor es realmente el mayor
    if palindromes:
        largest_found = palindromes[0][0]
        print(f"\n  Mayor palindrómico encontrado: {largest_found}")
        print(f"  {'✓ Coincide con el esperado' if largest_found == expected else '✗ Diferencia'}")
    
    # Análisis: rango de productos
    print("\nAnálisis:")
    print("  Rango de números de 2 dígitos: 10 a 99")
    print(f"  Producto mínimo: {10 * 10} = 10 × 10")
    print(f"  Producto máximo: {99 * 99} = 99 × 99 = {99 * 99}")
    print(f"  Mayor palindrómico: {expected}")
    
    # Solución del libro
    print("\nSolución del libro:")
    book_result = calculate_book()
    print(f"  calculate_book() = {book_result}")
    print(f"  {'✓ Coincide' if book_result == expected else '✗ Diferencia'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Como requiere el problema: llamar calculate() y imprimir el resultado
    print(calculate())
    
    # También ejecutar las pruebas detalladas
    main()


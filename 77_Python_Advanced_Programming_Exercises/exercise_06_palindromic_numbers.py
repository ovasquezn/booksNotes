"""
Exercise 06: Three-digit Palindromic Numbers

Descripción:
Consider the palindromic numbers. A palindromic or symmetric number is a number that 
does not change when you write its digits in reverse order.

Some examples of palindromic numbers:
• 363
• 2882
• 29492

Implement a function that returns the number of all three-digit palindromic numbers.

Requisitos:
- Implement a function that returns the number of all three-digit palindromic numbers
- Present the solution in the form of a function called calculate()
- Call calculate() function and print the result to the console

Ejemplo:
Expected result: 90

Three-digit palindromic numbers: 101, 111, 121, 131, ..., 191, 202, 212, ..., 999
Total count: 90
"""


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate():
    """
    Retorna el número de números palindrómicos de 3 dígitos.
    
    Un número palindrómico de 3 dígitos tiene la forma: aba
    donde a es el primer y último dígito (1-9) y b es el dígito del medio (0-9).
    
    Returns:
        int: El número de números palindrómicos de 3 dígitos (esperado: 90)
    """
    count = 0
    
    # Un número palindrómico de 3 dígitos tiene la forma: aba
    # donde a ∈ [1, 9] (no puede ser 0 porque sería de 2 dígitos)
    # y b ∈ [0, 9]
    
    for a in range(1, 10):  # Primer y último dígito (1-9)
        for b in range(10):  # Dígito del medio (0-9)
            # Construir el número: 100*a + 10*b + a = 101*a + 10*b
            number = 100 * a + 10 * b + a
            # Verificar que es palindrómico (aunque ya lo sabemos por construcción)
            if is_palindrome(number):
                count += 1
    
    return count


def calculate_direct():
    """
    Versión directa: simplemente contar las combinaciones.
    No necesitamos verificar, sabemos que todas las combinaciones aba son palindrómicas.
    
    Returns:
        int: El número de números palindrómicos de 3 dígitos
    """
    # 9 opciones para el primer/último dígito (1-9)
    # 10 opciones para el dígito del medio (0-9)
    return 9 * 10


def calculate_by_generation():
    """
    Versión que genera todos los números de 3 dígitos y verifica cuáles son palindrómicos.
    Menos eficiente pero más explícita.
    
    Returns:
        int: El número de números palindrómicos de 3 dígitos
    """
    count = 0
    for num in range(100, 1000):
        if is_palindrome(num):
            count += 1
    return count


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
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers)

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 06: Three-digit Palindromic Numbers")
    print("=" * 60)
    
    # Resultado esperado
    expected = 90
    
    print("\nResultado esperado: 90")
    print("\nVerificación de métodos:")
    
    # Método 1: Construcción directa
    result1 = calculate()
    print(f"\n  Método 1 (construcción): {result1}")
    print(f"    {'✓ Correcto' if result1 == expected else '✗ Incorrecto'}")
    
    # Método 2: Cálculo directo
    result2 = calculate_direct()
    print(f"\n  Método 2 (cálculo directo): {result2}")
    print(f"    {'✓ Correcto' if result2 == expected else '✗ Incorrecto'}")
    
    # Método 3: Generación y verificación
    result3 = calculate_by_generation()
    print(f"\n  Método 3 (generación): {result3}")
    print(f"    {'✓ Correcto' if result3 == expected else '✗ Incorrecto'}")
    
    # Verificar consistencia
    all_match = result1 == result2 == result3 == expected
    print(f"\n  {'✓ Todos los métodos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Mostrar algunos ejemplos de números palindrómicos de 3 dígitos
    print("\nEjemplos de números palindrómicos de 3 dígitos:")
    palindromes = []
    for a in range(1, 10):
        for b in range(10):
            num = 100 * a + 10 * b + a
            palindromes.append(num)
    
    print(f"  Total: {len(palindromes)} números")
    print(f"  Primeros 10: {palindromes[:10]}")
    print(f"  Últimos 10: {palindromes[-10:]}")
    print(f"  Algunos ejemplos: {palindromes[0]}, {palindromes[10]}, {palindromes[50]}, {palindromes[-1]}")
    
    # Verificar que todos son realmente palindrómicos
    print("\nVerificación: todos los números generados son palindrómicos:")
    all_are_palindromes = all(is_palindrome(num) for num in palindromes)
    print(f"  {'✓ Todos son palindrómicos' if all_are_palindromes else '✗ Algunos no son palindrómicos'}")
    
    # Verificar con método numérico también
    all_are_palindromes_numeric = all(is_palindrome_numeric(num) for num in palindromes)
    print(f"  {'✓ Verificación numérica también pasa' if all_are_palindromes_numeric else '✗ Error en verificación numérica'}")
    
    # Análisis: estructura de los números palindrómicos
    print("\nAnálisis de la estructura:")
    print("  Un número palindrómico de 3 dígitos tiene la forma: aba")
    print("  donde:")
    print("    - a ∈ [1, 9] (primer y último dígito, no puede ser 0)")
    print("    - b ∈ [0, 9] (dígito del medio)")
    print(f"  Total de combinaciones: 9 × 10 = {9 * 10}")
    
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


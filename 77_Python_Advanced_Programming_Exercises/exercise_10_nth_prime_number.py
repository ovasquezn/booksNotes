"""
Exercise 10: Prime Number at Position 100

Descripción:
A prime number is a natural number greater than 1 that is not a product of two 
smaller natural numbers.

Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...

The prime number in position one is 2. The prime number in position two is 3. 
The prime number in position three is 5. Implement a function that returns a 
prime number at position 100.

In the solution, use the function is_prime() from the previous exercise.

Requisitos:
- Implement a function that returns a prime number at position 100
- Use the is_prime() function from the previous exercise
- Present the solution in the form of a function called calculate()
- Call calculate() function and print the result to the console

Ejemplo:
Position 1: 2
Position 2: 3
Position 3: 5
Position 100: ?
"""


# ============================================================================
# FUNCIÓN is_prime() DEL EJERCICIO ANTERIOR
# ============================================================================

def is_prime(n):
    """
    Verifica si un número es primo (función proporcionada en el ejercicio).
    
    Args:
        n (int): Número natural a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# ============================================================================
# SOLUCIÓN PROPIA
# ============================================================================

def calculate():
    """
    Encuentra el número primo en la posición 100.
    
    Returns:
        int: El número primo en la posición 100
    """
    count = 0
    num = 2  # Empezar desde el primer número primo
    
    while count < 100:
        if is_prime(num):
            count += 1
            if count == 100:
                return num
        num += 1
    
    return None


def calculate_optimized():
    """
    Versión optimizada: saltar números pares después de 2.
    
    Returns:
        int: El número primo en la posición 100
    """
    count = 0
    num = 2
    
    # Contar el 2 primero
    if is_prime(num):
        count += 1
        if count == 100:
            return num
    
    # Continuar solo con números impares
    num = 3
    while count < 100:
        if is_prime(num):
            count += 1
            if count == 100:
                return num
        num += 2  # Solo probar números impares
    
    return None


def calculate_with_list():
    """
    Versión que genera una lista de los primeros 100 primos.
    
    Returns:
        int: El número primo en la posición 100
    """
    primes = []
    num = 2
    
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes[99]  # Índice 99 para el elemento 100


def get_nth_prime(n):
    """
    Función genérica para obtener el n-ésimo número primo.
    
    Args:
        n (int): Posición del número primo (1-indexed)
        
    Returns:
        int: El número primo en la posición n
    """
    if n < 1:
        return None
    
    count = 0
    num = 2
    
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
    
    return None


# ============================================================================
# SOLUCIÓN DEL LIBRO
# ============================================================================

def calculate_book():
    """
    Solución propuesta en el libro.
    """
    counter = 0
    number = 2
    while True:
        if is_prime(number):
            counter += 1
            if counter == 100:
                return number
        number += 1

# ============================================================================
# FUNCIÓN PRINCIPAL Y PRUEBAS
# ============================================================================

def main():
    """
    Función principal para probar las soluciones.
    """
    print("=" * 60)
    print("Exercise 10: Prime Number at Position 100")
    print("=" * 60)
    
    # Verificar los primeros primos
    print("\nVerificación de los primeros primos:")
    first_primes = []
    num = 2
    while len(first_primes) < 10:
        if is_prime(num):
            first_primes.append(num)
        num += 1
    
    print("  Posición | Número Primo")
    print("  " + "-" * 30)
    for i, prime in enumerate(first_primes, 1):
        print(f"  {i:8d} | {prime}")
    
    # Verificar posiciones conocidas
    print("\nVerificación de posiciones conocidas:")
    known_positions = [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (10, 29),
        (20, 71),
        (50, 229),
    ]
    
    for position, expected in known_positions:
        result = get_nth_prime(position)
        is_correct = result == expected
        status = "✓" if is_correct else "✗"
        print(f"  {status} Posición {position}: {result} (esperado: {expected})")
    
    # Encontrar el primo número 100
    print("\nBuscando el primo número 100:")
    result1 = calculate()
    result2 = calculate_optimized()
    result3 = calculate_with_list()
    
    print(f"  Método 1 (básico):     {result1}")
    print(f"  Método 2 (optimizado):  {result2}")
    print(f"  Método 3 (con lista):   {result3}")
    
    all_match = result1 == result2 == result3
    print(f"  {'✓ Todos los métodos coinciden' if all_match else '✗ Diferencia detectada'}")
    
    # Verificar que el resultado es realmente primo
    if result1:
        is_really_prime = is_prime(result1)
        print(f"\n  Verificación: ¿{result1} es primo? {is_really_prime}")
        print(f"  {'✓ Confirmado' if is_really_prime else '✗ Error'}")
    
    # Contar cuántos primos hay antes del resultado
    if result1:
        count_before = 0
        for num in range(2, result1):
            if is_prime(num):
                count_before += 1
        print(f"  Primos menores que {result1}: {count_before}")
        print(f"  {'✓ Correcto (debe ser 99)' if count_before == 99 else '✗ Error'}")
    
    # Lista de algunos primos alrededor de la posición 100
    print("\nPrimos alrededor de la posición 100:")
    positions = [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]
    print("  Posición | Número Primo")
    print("  " + "-" * 30)
    for pos in positions:
        prime = get_nth_prime(pos)
        marker = " <--" if pos == 100 else ""
        print(f"  {pos:8d} | {prime}{marker}")
    
    # Estadísticas
    print("\nEstadísticas:")
    if result1:
        print(f"  El primo número 100 es: {result1}")
        print(f"  Es el {result1}-ésimo número natural")
        print(f"  Hay {result1 - 100} números compuestos entre 1 y {result1}")
    
    # Solución del libro
    print("\nSolución del libro:")
    book_result = calculate_book()
    print(f"  calculate_book() = {book_result}")
    if result1:
        print(f"  {'✓ Coincide' if book_result == result1 else '✗ Diferencia'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Como requiere el problema: llamar calculate() y imprimir el resultado
    print(calculate())
    
    # También ejecutar las pruebas detalladas
    main()


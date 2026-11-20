def fizzbuzz(num):
    """
    Devuelve "fizz", "buzz", "fizzbuzz" o el mismo número, según corresponda.

    Reglas:
        - Si el número es divisible por 3 y por 5 a la vez, devuelve "fizzbuzz".
        - Si es divisible solo por 3, devuelve "fizz".
        - Si es divisible solo por 5, devuelve "buzz".
        - En cualquier otro caso, devuelve el número sin cambios.

    Parámetros:
        num (int): el número entero que se quiere evaluar.

    Retorna:
        str | int: "fizzbuzz", "fizz" o "buzz" si cumple alguna regla;
        si no, devuelve el mismo número recibido.

    Ejemplos:
        >>> fizzbuzz(15)
        'fizzbuzz'
        >>> fizzbuzz(9)
        'fizz'
        >>> fizzbuzz(10)
        'buzz'
        >>> fizzbuzz(7)
        7
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num == 0:
        return "fizzbuzz"
    return num
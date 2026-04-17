from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Возвращает n-е число Фибоначчи (начинается с 0)."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_sequence(n: int) -> list[int]:
    """Генерирует последовательность чисел Фибоначчи до n-го элемента."""
    return [fibonacci(i) for i in range(n)]
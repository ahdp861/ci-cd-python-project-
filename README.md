# Fibonacci Generator

Оптимизированный генератор чисел Фибоначчи на Python с поддержкой мемоизации и тестами на pytest.

---

## Описание

Этот проект предоставляет:

- Функцию для вычисления n-го числа Фибоначчи с мемоизацией (`@lru_cache`).
- Функцию для генерации последовательности чисел Фибоначчи до заданного индекса.
- Набор тестов для проверки корректности работы.

---

## Структура проекта

```
fibonacci/
├── src/fib.py       # Основной код генератора
├── tests/fib_test.py  # Тесты
├── requirements.txt   # Зависимости
├── .gitignore         # Игнорируемые файлы
└── README.md          # Документация
```

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/ahdp861/ci-cd-python-project-/edit/master/README.md
cd ci-cd-python-project-
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
pytest tests/fib_test -v
```

---

## Примеры использования

### Вычисление n-го числа Фибоначчи

```python
from fibonacci import fibonacci

print(fibonacci(10))  # Выведет: 55
```

### Генерация последовательности

```python
from fibonacci import generate_fibonacci_sequence

print(generate_fibonacci_sequence(10))
# Выведет: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Тестирование

Тесты покрывают:

- Базовые случаи (0, 1, 2).
- Положительные значения `n`.
- Генерацию последовательностей.
- Обработку ошибок (отрицательные `n`).



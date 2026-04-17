from src.fib import fibonacci, generate_fibonacci_sequence

def test_fibonacci_base_cases():  
    assert fibonacci(0) == 0  
    assert fibonacci(1) == 1  
    assert fibonacci(2) == 1

def test_fibonacci_positive_n():  
    assert fibonacci(5) == 5  
    assert fibonacci(10) == 55  
    assert fibonacci(15) == 610

def test_fibonacci_sequence():  
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]  
    assert generate_fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_negative_n():  
    try:  
        fibonacci(-1)  
        assert False, "Expected ValueError"  
    except ValueError:  
        pass

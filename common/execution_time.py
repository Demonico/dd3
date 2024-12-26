import time


def execution_time(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        diff = (end_time - start_time) * 1000
        print(f"execution time for {func.__name__}: {diff:.6f}ms")
        return result

    return wrapper

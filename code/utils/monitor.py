import time
import psutil

def measure_resources(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()
        start_cpu = process.cpu_percent(interval=None)
        start_memory = process.memory_info().rss
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_cpu = process.cpu_percent(interval=None)
        end_memory = process.memory_info().rss

        print(f"Function '{func.__name__}' took {end_time - start_time:.2f} seconds")
        print(f"Function '{func.__name__}' used {end_cpu - start_cpu:.2f}% CPU")
        print(f"Function '{func.__name__}' used {end_memory - start_memory} bytes of memory")
        
        return result
    return wrapper

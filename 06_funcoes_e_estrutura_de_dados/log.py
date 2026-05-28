import time
from loguru import logger
from functools import wraps

# Decorator de medida de tempo
def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            result = func(*args, **kwargs)
            return result
            
        except Exception as e:
            logger.exception(
                f"Erro na função '{func.__name}' | "
                f"Tipo: {type(e).__name__} | "
                f"Mensagem: {e}"
            )
            raise 

        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            logger.info(
                f"Função '{func.__name__}' executada em "
                f"{execution_time:.4} segundos"
            )

    return wrapper
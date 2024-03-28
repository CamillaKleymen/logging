import logging

logging.basicConfig(level=logging.ERROR,
                    filename='logerrors.log',
                    format="%(asctime)s | %(process)d | %(name)s | %(message)s")

def calc_multiply(a: int, m: int) -> dict:
    try:
        result = {'multiplication': a * m}
        return result
    except Exception as e:
        logging.error(f"Error occurred in calc_multiply: {e}")
        print(logging.error)

def calc_divide(a: int, m: int) -> dict:
    try:
        result = {'division': a / m}
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error occurred in calc_divide")
        print(logging.error)
    except Exception as e:
        logging.error(f"Error occurred in calc_divide: {e}")
        print(logging.error)

def calc_subtract(a: int, m: int) -> dict:
    try:
        result = {'subtraction': a - m}
        return result
    except Exception as e:
        logging.error(f"Error occurred in calc_subtract: {e}")
        print(logging.error)

print(calc_multiply(5, 25))
print(calc_divide(100, 25))
print(calc_subtract(171, 25))
print(calc_divide(10, 0))

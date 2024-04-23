def is_even_sum(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2 == 0:
            return True
        else: return False
    return wrapper
@is_even_sum
def get_sum(*args):
    return sum(args)

print(get_sum(1, 2, 3, 4))
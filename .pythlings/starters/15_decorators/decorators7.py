# decorators7
# Fix the program so it prints `LOG: total=12`.

# hint: Pass `*args` and `**kwargs` through, keep the label text as-is, and total the even numbers.
def make_label(prefix):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(args, kwargs)
            return prefix.lower() + result
        return wrapper
    return decorator


def require_odd_count(function):
    def wrapper(numbers):
        if len(numbers) % 2 == 0:
            return "bad"
        return function(numbers)
    return wrapper


@make_label("LOG: ")
@require_odd_count
def total_even_numbers(numbers):
    evens = [number for number in numbers if number % 2 == 1]
    return "total=" + str(sum(evens))


print(total_even_numbers([1, 2, 3, 4, 6]))

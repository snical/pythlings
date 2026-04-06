# decorators6
# Fix the program so it prints `<Ada>`.

# hint: Use both surrounding strings, and pass the name into the wrapped function.
def surround(left, right):
    def decorator(function):
        def wrapper(name):
            return left + function() + left
        return wrapper
    return decorator


@surround("<", ">")
def name_text(name):
    return name


print(name_text("Ada"))

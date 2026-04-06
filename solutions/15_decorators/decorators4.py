# decorators4
# Fix the program so it prints `[go!]`.

# hint: The `excited` decorator should add `!` before the `brackets` decorator runs.
def brackets(function):
    def wrapper():
        return "[" + function() + "]"
    return wrapper


def excited(function):
    def wrapper():
        return function() + "!"
    return wrapper


@brackets
@excited
def say():
    return "go"


print(say())

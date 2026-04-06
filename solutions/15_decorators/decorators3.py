# decorators3
# Fix the program so it prints `Ada has 7 points`.

# hint: Pass both arguments into the wrapped function.
def announce(function):
    def wrapper(name, points):
        return function(name, points)
    return wrapper


@announce
def build_message(name, points):
    return name + " has " + str(points) + " points"


print(build_message("Ada", 7))

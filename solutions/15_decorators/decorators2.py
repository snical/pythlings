# decorators2
# Fix the program so it prints `report: done!`.

# hint: The decorator adds `report: `, and the wrapped function should end with `!`.
def add_report(function):
    def wrapper():
        return "report: " + function()
    return wrapper


@add_report
def finish():
    return "done!"


print(finish())

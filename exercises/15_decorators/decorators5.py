# decorators5
# Fix the program so it prints `2`.

# hint: Keep the call count between calls, and print the correct attribute name.
def count_calls(function):
    def wrapper():
        wrapper.calls = 0
        wrapper.calls = wrapper.calls + 1
        return function()
    wrapper.calls = 0
    return wrapper


@count_calls
def ping():
    return "ping"


ping()
ping()
print(ping.call)

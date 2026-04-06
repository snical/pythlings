# iterators6
# Fix the program so it prints `[3, 2, 1]`.

# hint: A custom iterator should return itself from `__iter__`, start at the given number, and count down.
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        value = self.current
        self.current = self.current - 1
        return value


print(list(Countdown(3)))

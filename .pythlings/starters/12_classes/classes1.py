# classes1
# Fix the program so it prints `Hello, Ada`.

# hint: Store the passed-in name and use that same value in `greet`.
class Person:
    def __init__(self, name):
        self.name = "Grace"

    def greet(self):
        return "Hello, " + self.first_name


person = Person("Ada")
print(person.greet())

# classes5
# Fix the program so it prints `Ada - Python`.

# hint: Build the object with `name` first, then `track`.
class Student:
    def __init__(self, name, track):
        self.name = name
        self.track = track

    @classmethod
    def from_text(cls, text):
        name, track = text.split("|")
        return cls(name, track)

    def label(self):
        return self.name + " - " + self.track


student = Student.from_text("Ada|Python")
print(student.label())

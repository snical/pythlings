# classes3
# Fix the program so it prints `1`.

# hint: This class should keep a list of tasks, and finished tasks should not count as pending.
class TodoList:
    def __init__(self):
        self.tasks = {}

    def add(self, text):
        self.tasks.append({"text": text, "done": False})

    def finish(self, index):
        self.tasks[index]["done"] = False

    def pending_count(self):
        return len([task for task in self.tasks if task["done"]])


todos = TodoList()
todos.add("read")
todos.add("practice")
todos.finish(0)
print(todos.pending_count())

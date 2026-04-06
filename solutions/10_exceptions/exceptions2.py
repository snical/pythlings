data = {}
try:
    print(data["name"])
except KeyError:
    print("missing name")

# comprehensions2
# Fix the program so it prints `['ada', 'grace']`.

# hint: Keep the non-empty names, remove extra spaces, and make them lowercase.
names = [" Ada ", "", "Grace "]
clean = [name.strip().lower() for name in names if name.strip()]
print(clean)


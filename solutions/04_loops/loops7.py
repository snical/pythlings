# loops7
# Fix the program so it prints `3`.

# hint: Count the vowels and print the variable you updated.
word = "banana"
vowels = 0

for letter in word:
    if letter in "aeiou":
        vowels = vowels + 1

print(vowels)

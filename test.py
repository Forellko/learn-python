# Ask name
name = input("What is your name? ").title().strip()

# Split user's name into first name and last name
first, last = name.split()

# Print Hello
print(f"Hello, {first}" )
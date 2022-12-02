true_false = True
words = ""

# print("Hello world!")

print("Is Gareth awesome?")

s = input('> ')

if (s == "True" or s == "true" or s == "yes"):
    true_false = True
else:
    true_false = False

if true_false:
    words = "Gareth is awesome!"
else:
    words = "Gareth is not awesome. Awww...we'll fix that."

print(words)

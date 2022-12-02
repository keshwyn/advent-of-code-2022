true_false = True
words = ""
answer = ""

# Function makes Gareth awesome - no matter what.
# Returns either 'Gareth is awesome', or 'Answer rejected: Gareth is awesome!'
def make_gareth_awesome():
    print("Is Gareth awesome (second try)?")
    answer = ""
    while not answer:
        s = input('> ')
        if s == '':
            print("No, you have to tell us whether Gareth is awesome or not. Try again.")
        else:
            answer = s

        if (answer == "True" or answer == "true" or answer == "yes"):
            true_false = True
        else:
            true_false = False

    if true_false != True:
        return "Your answer is rejected: Gareth is awesome!"
    else:
        return "Wise choice: Gareth is indeed awesome!"

# Main body of code
print("Is Gareth awesome?")
answer = ""
while not answer:
    s = input('> ')
    if s == '':
        print ("No, you have to tell us whether Gareth is awesome or not. Try again.")
    else:
        answer = s

    if (answer == "True" or answer == "true" or answer == "yes"):
        true_false = True
    else:
        true_false = False

if true_false:
    words = "Gareth is awesome!"
else:
    print("Gareth is not awesome. Awww...we'll fix that.")
    words = make_gareth_awesome()

print(words)
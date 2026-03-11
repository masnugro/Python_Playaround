import random
print("find the missing letter")
print("")
score = 0
rounds = 3
for i in range(rounds):
    missing = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    alphabet = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter == missing:
            alphabet.append("_")
            random.shuffle(alphabet)
        else:
            alphabet.append(letter)
    print(f"round {i+1} of {rounds}")
    print(" ".join(alphabet))

    guess = input("which letter is missing?").upper().strip()
    if guess == missing:
        print("correct!")
        score += 1
    else:
        print(f"find a new family and you can't eat dinner! the missing letter was {missing}")
    print("")

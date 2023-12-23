from random import randrange

calculation = 3
right = 0
wrong = 0

print(f"Du bekommt {calculation} Rechenaufgaben")

for _ in range(calculation):
    number_1 = randrange(4)
    number_2 = randrange(5)

    print(f"Was ist {number_1 + 1} + {number_2 + 1}?")
    result = input()

    if int(result) == (number_1 + 1 + number_2 + 1):
        print("Richtig!")
        right += 1
    else:
        print(f"Falsch: {number_1 + 1} + {number_2 + 1} = {number_1 + 1 + number_2 + 1}")
        wrong += 1

print(f"Du hast {right} Aufgaben richtig gerechnet und {wrong} Aufgaben waren falsch.")

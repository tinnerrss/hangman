import random

  turns = 9
  words = ['sleepy', 'confused', 'uncertain', 'impatient', 'hungry']
  random_word = random.choice(words)
  guesses = []

  while turns > 0:
    print(random_word)
    print("Enter a letter:")
    x = input()


    if x in random_word:
      guesses.append(x)
      print(guesses)
      print(f"{turns} turns left")
    else:
      print("NOPE")
      print(f"{turns} turns left")
    turns -= 1



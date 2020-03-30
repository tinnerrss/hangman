import random

turns = 9
words = ['sleepy', 'confused', 'uncertain', 'impatient', 'hungry']
random_word = random.choice(words)
guesses = []
show = []
show.extend(random_word)



print(guesses)

for letter in range (len(show)):
  show[letter] = "_"

print(' '.join(show))
print()


while turns > 0:
  print(random_word)
  print("Guess a letter:")
  x = input()

  for i in range(len(random_word)):
    if random_word == guesses:
      show == guesses

  print(' '.join(show))



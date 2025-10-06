import random
word_list = ["aardvarkk", "baboonn", "camell"]

chosen_word = random.choice(word_list)
print(chosen_word)
chosen_word_chars = list(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word


answer = []
guess = ""
guessIndex = 0
iteration = 0

for letter in chosen_word_chars:
  answer.append("_")

while "".join(answer) != chosen_word:
  letterFound = False
  guess = input("Guess a letter: ").lower()
  iteration += 1

  for letter in chosen_word_chars:
    while not letterFound:
      try:
        guessIndex = chosen_word_chars.index(guess)
        print(guess + " found at index " + str(guessIndex))
        answer[guessIndex] = guess.upper()
        chosen_word_chars[guessIndex] = ""
      except ValueError:
        break
  print(f"Answer: {"".join(answer)}")


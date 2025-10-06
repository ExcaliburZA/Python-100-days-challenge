alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original, shift_amt):
  chars = list(original)
  encrypted = []

  for letter in chars:
    if letter not in alphabet:
      encrypted.append(letter)
    else:
      shifted_index = alphabet.index(letter) + shift_amt

      if shifted_index > (len(alphabet) - 1):
        print(str(shifted_index) + " exceeds the index range of " + str(len(alphabet) - 1))
        shifted_index = shifted_index - (len(alphabet))

      encrypted.append(alphabet[shifted_index])
  return "".join(encrypted)

def decrypt(encrypted, shift_amt):
  chars = list(encrypted)
  decrypted = []

  for letter in chars:
    if letter not in alphabet:
      encrypted.append(letter)
    else:
      shifted_index = alphabet.index(letter) - shift_amt

      if shifted_index < 0:
        print(str(shifted_index) + " exceeds the index range of " + str(
          len(alphabet) - 1))
        shifted_index = len(alphabet) - (len(alphabet) - shifted_index)

      decrypted.append(alphabet[shifted_index])
  return "".join(decrypted)


if direction == "encode":
  encryptedResponse = encrypt(text, shift)
  print("Encrypted: " + encryptedResponse)
else:
  decryptedResponse = decrypt(text, shift)
  print("Decrypted: " + decryptedResponse)


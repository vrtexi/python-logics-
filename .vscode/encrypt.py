import string 
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("enter a message to encrypt: ")
cipher_text = ''

for letters in plain_text:
  index = chars.index(letters)
  cipher_text += key[index]
  
print(f"encrypted messages : {cipher_text}")

cipher_text = input("enter a message to decrypt: ")
plain_text = ''

for letters in cipher_text:
  index = key.index(letters)
  plain_text += chars[index]
  
print(f"encrypted messages : {plain_text}")
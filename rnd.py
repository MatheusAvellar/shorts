import string
import random

# Alphabet minus l
ALPHABET = "abcdefghijkmnopqrstuvwxyz" + string.digits + '_'
N = 5

# [Ref] stackoverflow.com/a/2257449/4824627
def genID():
  return "".join(random.choice(ALPHABET) for _ in range(N))

while True:
  print(genID(), end="")
  input()
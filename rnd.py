import string
import random

# Alphabet minus l
ALPHANUM_HYPH = "abcdefghijkmnopqrstuvwxyz" + string.digits + '-'
ALPHANUM = "abcdefghijkmnopqrstuvwxyz" + string.digits
N = 5

# [Ref] stackoverflow.com/a/2257449/4824627
def genID():
  return "".join([
    random.choice(ALPHANUM),
    "".join(random.choice(ALPHANUM_HYPH) for _ in range(N-2)),
    random.choice(ALPHANUM)
  ]).replace("--", "-" + random.choice(ALPHANUM))

while True:
  print(genID(), end="")
  input()
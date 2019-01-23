import string
print(string.ascii_letters)
print(string.ascii_lowercase)

#We want a random seection hence the random module

import random
print(random.choice("pull a letter from here"))
print(random.choice(string.ascii_lowercase))
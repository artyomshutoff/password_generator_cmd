import string
from random import choice
chars = string.ascii_letters + string.digits
print(''.join([choice(chars) for i in range(16)]))

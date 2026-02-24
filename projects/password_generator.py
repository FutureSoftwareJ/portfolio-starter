import random
import string

# Generate a random password
length = 12  # You can change this number

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Your generated password is:", password)

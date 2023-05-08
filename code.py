import random
import string

length = int(input("enter a length: "))
def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

print(generate_password(length))

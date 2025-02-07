import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

demo_data = {}
for i in range(1, 6):
    user_id = f"user{i}"
    password = generate_password()
    demo_data[user_id] = password

for user_id, password in demo_data.items():
    print(f"ID: {user_id}, Password: {password}")
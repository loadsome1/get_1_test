import random
import string


# Функция для генерации случайного пароля
def generate_password(length=12):
    # Определяем символы для пароля
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    # Генерируем пароль
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


# Генерируем 5 паролей
for i in range(5):
    pwd = generate_password()
    print(f"Пароль {i + 1}: {pwd}")
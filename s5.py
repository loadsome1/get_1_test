import random


# Игра "Угадай число"
def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = int(input("Введи число: "))
        attempts += 1
        if guess < number:
            print("Слишком мало!")
        elif guess > number:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Ты угадал число {number} за {attempts} попыток!")
            break


# Запускаем игру
guess_number()
# Простой калькулятор с основными операциями
def calculator():
    print("Выберите операцию: +, -, *, /")
    operation = input("Введите операцию: ")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выполняем выбранную операцию
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль!"
    else:
        result = "Неверная операция!"

    print(f"Результат: {result}")


# Запускаем калькулятор
calculator()
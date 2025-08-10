# Функция для подсчёта слов в тексте
def count_words(text):
    # Разбиваем текст на слова
    words = text.split()
    # Подсчитываем количество слов
    word_count = len(words)
    # Создаём словарь для подсчёта частоты слов
    word_freq = {}
    for word in words:
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_count, word_freq

# Тестируем функцию
text = "Это пример текста. Пример текста для анализа."
total, freq = count_words(text)
print(f"Общее количество слов: {total}")
print("Частота слов:")
for word, count in freq.items():
    print(f"{word}: {count}")
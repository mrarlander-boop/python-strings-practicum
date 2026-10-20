"""
Задание 1: Подсчёт частоты слов
Описание:
Введите предложение. Определите, сколько раз встречается каждое слово.
Регистр букв и знаки препинания не учитывайте. Выведите слова и количество их повторений.

Пример:
Ввод: Python удобен, Python понятен и python популярен.
Вывод: python — 3; удобен — 1; понятен — 1; и — 1; популярен — 1
"""

import string


def count_word_frequency(text: str) -> dict[str, int]:
    """
    Очищает текст от знаков препинания, переводит в нижний регистр
    и подсчитывает частоту слов в порядке их первого появления.
    """
    # 1. Формируем расширенный набор знаков препинания (включая тире и кавычки)
    punctuation_to_remove = string.punctuation + "—–«»„“”"
    
    # 2. Заменяем знаки препинания на пробелы, чтобы не склеивать слова
    cleaned_chars = [
        " " if char in punctuation_to_remove else char
        for char in text
    ]
    cleaned_text = "".join(cleaned_chars)
    
    # 3. Приводим к нижнему регистру и разбиваем на слова
    words = cleaned_text.lower().split()
    
    # 4. Подсчитываем количество повторений каждого слова с помощью словаря
    frequency_dict: dict[str, int] = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
        
    return frequency_dict


def format_word_frequency(frequency_dict: dict[str, int]) -> str:
    """
    Форматирует словарь частот в строку согласно требованиям задания.
    """
    if not frequency_dict:
        return "Слова не найдены"
    return "; ".join(f"{word} — {count}" for word, count in frequency_dict.items())


def main() -> None:
    print("=== Задание 1: Подсчёт частоты слов ===")
    user_input = input("Введите предложение: ")
    freq = count_word_frequency(user_input)
    result = format_word_frequency(freq)
    print(f"Вывод: {result}")


if __name__ == "__main__":
    main()

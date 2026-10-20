"""
Задание 12: Статистика текста
Описание:
Введите строку и подсчитайте количество слов, букв, цифр и знаков препинания.
Пробелы не относите ни к одной категории.

Пример:
Ввод: Python 3 — отличный язык!
Вывод: Слов: 4; букв: 18; цифр: 1; знаков препинания: 2
"""

import string


PUNCTUATION_SET = set(string.punctuation + "—–«»„“”…" + "№")


def calculate_text_statistics(text: str) -> dict[str, int]:
    """
    Подсчитывает в строке:
    - количество слов (токены, содержащие буквы или цифры);
    - количество букв (isalpha);
    - количество цифр (isdigit);
    - количество знаков препинания (принадлежность к набору пунктуации).
    Пробельные символы не относятся ни к одной категории.
    """
    letters_count = 0
    digits_count = 0
    punctuation_count = 0
    
    # Подсчёт по символам
    for char in text:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char in PUNCTUATION_SET:
            punctuation_count += 1
            
    # Подсчёт слов: разбиваем по пробелам и отбираем токены, содержащие буквенно-цифровые символы
    raw_tokens = text.split()
    words = [
        token for token in raw_tokens
        if any(c.isalnum() for c in token)
    ]
    words_count = len(words)
    
    return {
        "words": words_count,
        "letters": letters_count,
        "digits": digits_count,
        "punctuation": punctuation_count,
    }


def format_text_statistics(stats: dict[str, int]) -> str:
    """
    Форматирует статистику в строку вида:
    'Слов: 4; букв: 18; цифр: 1; знаков препинания: 2'
    """
    return (
        f"Слов: {stats['words']}; "
        f"букв: {stats['letters']}; "
        f"цифр: {stats['digits']}; "
        f"знаков препинания: {stats['punctuation']}"
    )


def main() -> None:
    print("=== Задание 12: Статистика текста ===")
    user_input = input("Введите строку: ")
    stats = calculate_text_statistics(user_input)
    print(f"Вывод: {format_text_statistics(stats)}")


if __name__ == "__main__":
    main()

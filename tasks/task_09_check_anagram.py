"""
Задание 9: Проверка анаграмм
Описание:
Введите две строки и определите, являются ли они анаграммами.
Не учитывайте пробелы, знаки препинания и регистр букв.

Пример:
Ввод: Апельсин; Спаниель
Вывод: Это анаграммы
"""


def extract_normalized_letters(text: str) -> list[str]:
    """
    Извлекает из строки только буквы, приводит их к нижнему регистру
    и возвращает отсортированный список.
    """
    return sorted(char.lower() for char in text if char.isalpha())


def are_anagrams(first_text: str, second_text: str) -> bool:
    """
    Проверяет, являются ли две строки анаграммами без учёта пробелов,
    пунктуации и регистра букв.
    """
    letters_first = extract_normalized_letters(first_text)
    letters_second = extract_normalized_letters(second_text)
    
    # Если букв вообще нет, строчки не считаются анаграммами
    if not letters_first or not letters_second:
        return False
        
    return letters_first == letters_second


def check_anagram_message(first_text: str, second_text: str) -> str:
    """
    Возвращает строковый вердикт проверки на анаграмму.
    """
    return "Это анаграммы" if are_anagrams(first_text, second_text) else "Это не анаграммы"


def main() -> None:
    print("=== Задание 9: Проверка анаграмм ===")
    first_input = input("Введите первую строку (или две строки через ';'): ")
    
    if ";" in first_input:
        parts = first_input.split(";", 1)
        str1, str2 = parts[0].strip(), parts[1].strip()
    else:
        str1 = first_input.strip()
        str2 = input("Введите вторую строку: ").strip()
        
    result = check_anagram_message(str1, str2)
    print(f"Вывод: {result}")


if __name__ == "__main__":
    main()

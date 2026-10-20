"""
Задание 8: Чередование регистра
Описание:
Введите строку. Измените регистр букв так, чтобы первая буква стала
прописной, вторая — строчной, третья — прописной и так далее.
Пробелы и знаки препинания не должны влиять на чередование.

Пример:
Ввод: python — это интересно!
Вывод: PyThOn — ЭтО иНтЕрЕсНо!
"""


def alternate_case(text: str) -> str:
    """
    Преобразует буквы строки так, чтобы они чередовали регистр:
    нечётная буква (1-я, 3-я, ...) — заглавная,
    чётная буква (2-я, 4-я, ...) — строчная.
    Пробелы и пунктуация не сбивают счётчик.
    """
    letter_index = 0
    result_chars: list[str] = []
    
    for char in text:
        if char.isalpha():
            if letter_index % 2 == 0:
                result_chars.append(char.upper())
            else:
                result_chars.append(char.lower())
            letter_index += 1
        else:
            result_chars.append(char)
            
    return "".join(result_chars)


def main() -> None:
    print("=== Задание 8: Чередование регистра ===")
    user_input = input("Введите строку: ")
    result = alternate_case(user_input)
    print(f"Вывод: {result}")


if __name__ == "__main__":
    main()

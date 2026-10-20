"""
Задание 4: Удаление соседних повторов
Описание:
Введите предложение, в котором некоторые слова могут повторяться подряд.
Удалите соседние повторы без учёта регистра, сохранив первое написание слова.

Пример:
Ввод: Мы мы изучаем Python python каждый день
Вывод: Мы изучаем Python каждый день
"""


def remove_adjacent_duplicates(text: str) -> str:
    """
    Удаляет последовательно идущие дубликаты слов без учёта регистра,
    сохраняя исходный регистр первого вхождения слова.
    """
    words = text.split()
    if not words:
        return ""
        
    unique_adjacent_words: list[str] = []
    
    for word in words:
        # Сравниваем с последним добавленным словом без учёта регистра
        if not unique_adjacent_words or word.lower() != unique_adjacent_words[-1].lower():
            unique_adjacent_words.append(word)
            
    return " ".join(unique_adjacent_words)


def main() -> None:
    print("=== Задание 4: Удаление соседних повторов ===")
    user_input = input("Введите предложение: ")
    result = remove_adjacent_duplicates(user_input)
    print(f"Вывод: {result}")


if __name__ == "__main__":
    main()

"""
Задание 2: Самый частый символ
Описание:
Введите строку и найдите символ, который встречается чаще всего.
Пробелы не учитывайте. Если лидеров несколько, выведите тот, который встретился раньше.

Пример:
Ввод: программирование
Вывод: р — 3
"""


def find_most_frequent_char(text: str) -> tuple[str, int] | None:
    """
    Находит символ, встречающийся чаще всего, исключая пробелы.
    При равенстве частот возвращает символ, встретившийся раньше.
    """
    # 1. Подсчитываем количество каждого символа в словаре
    char_counts: dict[str, int] = {}
    for char in text:
        # Пробелы не учитываем
        if char == " " or char.isspace():
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Если символов нет
    if not char_counts:
        return None
        
    # 2. Находим символ с максимальной частотой.
    # Так как max() в Python возвращает первый элемент при равенстве,
    # а dict сохраняет порядок добавления, будет выбран первый встретившийся лидер.
    best_char = max(char_counts, key=char_counts.get)
    return best_char, char_counts[best_char]


def format_most_frequent_char(result: tuple[str, int] | None) -> str:
    """
    Форматирует результат поиска самого частого символа.
    """
    if result is None:
        return "Символы не найдены"
    char, count = result
    return f"{char} — {count}"


def main() -> None:
    print("=== Задание 2: Самый частый символ ===")
    user_input = input("Введите строку: ")
    result = find_most_frequent_char(user_input)
    print(f"Вывод: {format_most_frequent_char(result)}")


if __name__ == "__main__":
    main()

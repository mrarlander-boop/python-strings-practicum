"""
Задание 7: Сумма чисел в тексте
Описание:
Введите строку, содержащую слова и целые положительные числа.
Найдите все последовательности цифр и вычислите сумму найденных чисел.

Пример:
Ввод: В группе 18 студентов, из них 7 отличников
Вывод: 25
"""


def sum_numbers_in_text(text: str) -> int:
    """
    Находит все последовательности цифр в строке
    и возвращает их сумму.
    """
    total_sum = 0
    current_digits = ""
    
    for char in text:
        if char.isdigit():
            # Накапливаем цифры текущего числа
            current_digits += char
        else:
            # Если встретился нецифровой символ и число было накоплено
            if current_digits:
                total_sum += int(current_digits)
                current_digits = ""
                
    # Если строка оканчивается числом, прибавляем его
    if current_digits:
        total_sum += int(current_digits)
        
    return total_sum


def main() -> None:
    print("=== Задание 7: Сумма чисел в тексте ===")
    user_input = input("Введите строку: ")
    total = sum_numbers_in_text(user_input)
    print(f"Вывод: {total}")


if __name__ == "__main__":
    main()

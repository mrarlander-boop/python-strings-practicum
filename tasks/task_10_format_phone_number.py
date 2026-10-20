"""
Задание 10: Форматирование номера телефона
Описание:
Введите номер телефона в произвольном виде. Оставьте только цифры.
Если получено 11 цифр, выведите номер в формате +7 (XXX) XXX-XX-XX;
начальную 8 замените на 7.

Пример:
Ввод: 8 701 234 56 78
Вывод: +7 (701) 234-56-78
"""


def format_phone_number(raw_phone: str) -> str:
    """
    Извлекает цифры из строки и форматирует их в стандартный вид:
    +7 (XXX) XXX-XX-XX. Если получено не 11 цифр, возвращает сообщение об ошибке.
    """
    # 1. Извлекаем только цифры с помощью isdigit()
    digits = "".join(char for char in raw_phone if char.isdigit())
    
    # 2. Проверяем длину
    if len(digits) != 11:
        return f"Ошибка: номер должен содержать ровно 11 цифр (получено {len(digits)})"
        
    # 3. Заменяем начальную 8 на 7
    if digits[0] == "8":
        digits = "7" + digits[1:]
    elif digits[0] != "7":
        digits = "7" + digits[1:]
        
    # 4. Применяем срезы для формирования маски +7 (XXX) XXX-XX-XX
    area_code = digits[1:4]
    first_part = digits[4:7]
    second_part = digits[7:9]
    third_part = digits[9:11]
    
    return f"+7 ({area_code}) {first_part}-{second_part}-{third_part}"


def main() -> None:
    print("=== Задание 10: Форматирование номера телефона ===")
    user_input = input("Введите номер телефона: ")
    formatted = format_phone_number(user_input)
    print(f"Вывод: {formatted}")


if __name__ == "__main__":
    main()

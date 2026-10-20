"""
Задание 5: Проверка адреса электронной почты
Описание:
Введите адрес электронной почты. Считайте его корректным, если в нём
один символ @, до и после него есть текст, а часть после @ содержит
точку не в начале и не в конце.

Пример:
Ввод: student@example.com
Вывод: Корректный адрес
"""


def is_valid_email(email: str) -> bool:
    """
    Проверяет корректность email по заданным критериям:
    1. Ровно один символ '@'
    2. Текст до '@' не пустой
    3. Текст после '@' не пустой
    4. Текст после '@' содержит точку не на первом и не на последнем месте.
    """
    # 1. Проверяем, что символ '@' встречается ровно один раз
    if email.count("@") != 1:
        return False
        
    username, domain = email.split("@")
    
    # 2. До и после '@' должен быть текст
    if len(username) == 0 or len(domain) == 0:
        return False
        
    # 3. В доменной части должна быть точка, но не в начале и не в конце
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
        
    return True


def check_email_message(email: str) -> str:
    """
    Возвращает текстовый вердикт проверки email.
    """
    return "Корректный адрес" if is_valid_email(email) else "Некорректный адрес"


def main() -> None:
    print("=== Задание 5: Проверка адреса электронной почты ===")
    user_input = input("Введите адрес электронной почты: ").strip()
    result = check_email_message(user_input)
    print(f"Вывод: {result}")


if __name__ == "__main__":
    main()

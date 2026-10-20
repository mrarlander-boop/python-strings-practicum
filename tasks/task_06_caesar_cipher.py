"""
Задание 6: Шифр Цезаря
Описание:
Введите строку из латинских букв и целое число сдвига.
Замените каждую букву буквой, расположенной на указанное количество
позиций дальше в алфавите. После Z переходите к A. Сохраняйте регистр.

Пример:
Ввод: Python, сдвиг: 3
Вывод: Sbwkrq
"""


def caesar_cipher(text: str, shift: int) -> str:
    """
    Выполняет шифрование строки шифром Цезаря с сохранением регистра
    для латинских букв.
    """
    # Приводим сдвиг к диапазону [0, 25]
    effective_shift = shift % 26
    encrypted_chars: list[str] = []
    
    for char in text:
        if "a" <= char <= "z":
            # Смещение для строчных латинских букв
            base = ord("a")
            new_code = base + (ord(char) - base + effective_shift) % 26
            encrypted_chars.append(chr(new_code))
        elif "A" <= char <= "Z":
            # Смещение для заглавных латинских букв
            base = ord("A")
            new_code = base + (ord(char) - base + effective_shift) % 26
            encrypted_chars.append(chr(new_code))
        else:
            # Все прочие символы остаются без изменений
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)


def main() -> None:
    print("=== Задание 6: Шифр Цезаря ===")
    user_text = input("Введите строку: ")
    try:
        user_shift = int(input("Введите целое число сдвига: "))
    except ValueError:
        print("Ошибка: сдвиг должен быть целым числом.")
        return
        
    encrypted = caesar_cipher(user_text, user_shift)
    print(f"Вывод: {encrypted}")


if __name__ == "__main__":
    main()

"""
Автоматизированное тестирование всех 12 заданий по строкам.
Каждое задание проверяется минимум на 3 наборах данных,
включая эталонный пример из задания и граничный случай.
"""

from tasks.task_01_word_frequency import count_word_frequency, format_word_frequency
from tasks.task_02_most_frequent_char import find_most_frequent_char, format_most_frequent_char
from tasks.task_03_normalize_sentence import normalize_sentence
from tasks.task_04_remove_adjacent_duplicates import remove_adjacent_duplicates
from tasks.task_05_check_email import check_email_message
from tasks.task_06_caesar_cipher import caesar_cipher
from tasks.task_07_sum_numbers_in_text import sum_numbers_in_text
from tasks.task_08_alternate_case import alternate_case
from tasks.task_09_check_anagram import check_anagram_message
from tasks.task_10_format_phone_number import format_phone_number
from tasks.task_11_longest_common_prefix import find_longest_common_prefix
from tasks.task_12_text_statistics import calculate_text_statistics, format_text_statistics


def test_task_01() -> None:
    print("\n--- Тестирование Задания 1: Подсчёт частоты слов ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "Python удобен, Python понятен и python популярен."
    res1 = format_word_frequency(count_word_frequency(inp1))
    assert res1 == "python — 3; удобен — 1; понятен — 1; и — 1; популярен — 1", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Обычный)
    inp2 = "Кот, собака, кот; собака, собака!"
    res2 = format_word_frequency(count_word_frequency(inp2))
    assert res2 == "кот — 2; собака — 3", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Обычный): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: только знаки препинания и пробелы)
    inp3 = "  ... ,,, --- !  "
    res3 = format_word_frequency(count_word_frequency(inp3))
    assert res3 == "Слова не найдены", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - без слов): '{inp3}' -> '{res3}'")


def test_task_02() -> None:
    print("\n--- Тестирование Задания 2: Самый частый символ ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "программирование"
    res1 = format_most_frequent_char(find_most_frequent_char(inp1))
    assert res1 == "р — 3", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Несколько лидеров с одинаковой частотой - побеждает первый)
    inp2 = "бб аа вв"
    res2 = format_most_frequent_char(find_most_frequent_char(inp2))
    assert res2 == "б — 2", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Равенство лидеров): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: только пробелы)
    inp3 = "     "
    res3 = format_most_frequent_char(find_most_frequent_char(inp3))
    assert res3 == "Символы не найдены", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - только пробелы): '{inp3}' -> '{res3}'")


def test_task_03() -> None:
    print("\n--- Тестирование Задания 3: Нормализация предложения ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "пРИВЕТ, МИР"
    res1 = normalize_sentence(inp1)
    assert res1 == "Привет, мир.", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Множество пробелов и точка уже есть)
    inp2 = "   хОРОШАЯ   погода   СЕГОДНЯ.   "
    res2 = normalize_sentence(inp2)
    assert res2 == "Хорошая погода сегодня.", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Множественные пробелы и точка): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: пустая строка)
    inp3 = "     "
    res3 = normalize_sentence(inp3)
    assert res3 == "", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - пустая строка): '{inp3}' -> '{res3}'")


def test_task_04() -> None:
    print("\n--- Тестирование Задания 4: Удаление соседних повторов ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "Мы мы изучаем Python python каждый день"
    res1 = remove_adjacent_duplicates(inp1)
    assert res1 == "Мы изучаем Python каждый день", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Не подряд идущие повторы НЕ должны удаляться)
    inp2 = "да да нет да ДА"
    res2 = remove_adjacent_duplicates(inp2)
    assert res2 == "да нет да", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Повторы в разных местах): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: тройной повтор одного слова)
    inp3 = "Тест тест ТЕСТ"
    res3 = remove_adjacent_duplicates(inp3)
    assert res3 == "Тест", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - тройной повтор): '{inp3}' -> '{res3}'")


def test_task_05() -> None:
    print("\n--- Тестирование Задания 5: Проверка email ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "student@example.com"
    res1 = check_email_message(inp1)
    assert res1 == "Корректный адрес", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Корректный с поддоменом)
    inp2 = "user.name@sub.domain.org"
    res2 = check_email_message(inp2)
    assert res2 == "Корректный адрес", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Поддомен): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: точка в начале домена или несколько @)
    assert check_email_message("user@.com") == "Некорректный адрес"
    assert check_email_message("user@domain.") == "Некорректный адрес"
    assert check_email_message("@domain.com") == "Некорректный адрес"
    assert check_email_message("user@@domain.com") == "Некорректный адрес"
    print("[OK] Тест 3 (Граничные некорректные адреса): успешно отсеяны")


def test_task_06() -> None:
    print("\n--- Тестирование Задания 6: Шифр Цезаря ---")
    
    # Тест 1 (Пример из задания)
    inp1, shift1 = "Python", 3
    res1 = caesar_cipher(inp1, shift1)
    assert res1 == "Sbwkrq", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}', {shift1} -> '{res1}'")
    
    # Тест 2 (Переход через границу Z -> A)
    inp2, shift2 = "xyzXYZ", 3
    res2 = caesar_cipher(inp2, shift2)
    assert res2 == "abcABC", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Переход Z->A): '{inp2}', {shift2} -> '{res2}'")
    
    # Тест 3 (Граничный: сдвиг на 0 или полный оборот на 26)
    inp3, shift3 = "Hello, World!", 26
    res3 = caesar_cipher(inp3, shift3)
    assert res3 == "Hello, World!", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - сдвиг 26): '{inp3}', {shift3} -> '{res3}'")


def test_task_07() -> None:
    print("\n--- Тестирование Задания 7: Сумма чисел в тексте ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "В группе 18 студентов, из них 7 отличников"
    res1 = sum_numbers_in_text(inp1)
    assert res1 == 25, f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> {res1}")
    
    # Тест 2 (Несколько чисел подряд и на границах)
    inp2 = "10 яблок 20 груш и 100 грамм"
    res2 = sum_numbers_in_text(inp2)
    assert res2 == 130, f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Число в начале и в конце): '{inp2}' -> {res2}")
    
    # Тест 3 (Граничный: чисел нет вообще)
    inp3 = "Просто текст без единой цифры!"
    res3 = sum_numbers_in_text(inp3)
    assert res3 == 0, f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - без чисел): '{inp3}' -> {res3}")


def test_task_08() -> None:
    print("\n--- Тестирование Задания 8: Чередование регистра ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "python — это интересно!"
    res1 = alternate_case(inp1)
    assert res1 == "PyThOn — ЭтО иНтЕрЕсНо!", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Обычная строка)
    inp2 = "hello world"
    res2 = alternate_case(inp2)
    assert res2 == "HeLlO wOrLd", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Строка): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: строка без букв)
    inp3 = "12345 -- !?..."
    res3 = alternate_case(inp3)
    assert res3 == "12345 -- !?...", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - без букв): '{inp3}' -> '{res3}'")


def test_task_09() -> None:
    print("\n--- Тестирование Задания 9: Проверка анаграмм ---")
    
    # Тест 1 (Пример из задания)
    str1_1, str1_2 = "Апельсин", "Спаниель"
    res1 = check_anagram_message(str1_1, str1_2)
    assert res1 == "Это анаграммы", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{str1_1}' и '{str1_2}' -> '{res1}'")
    
    # Тест 2 (С пробелами, знаками препинания и разным регистром)
    str2_1, str2_2 = "Я в раю!", "Юра, вя!"
    res2 = check_anagram_message(str2_1, str2_2)
    assert res2 == "Это анаграммы", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (С пунктуацией): '{str2_1}' и '{str2_2}' -> '{res2}'")
    
    # Тест 3 (Граничный: не анаграммы с похожими буквами)
    str3_1, str3_2 = "тест", "тесто"
    res3 = check_anagram_message(str3_1, str3_2)
    assert res3 == "Это не анаграммы", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - не анаграммы): '{str3_1}' и '{str3_2}' -> '{res3}'")


def test_task_10() -> None:
    print("\n--- Тестирование Задания 10: Форматирование телефона ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "8 701 234 56 78"
    res1 = format_phone_number(inp1)
    assert res1 == "+7 (701) 234-56-78", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Уже с +7, скобками и тире)
    inp2 = "+7 (999) 111-22-33"
    res2 = format_phone_number(inp2)
    assert res2 == "+7 (999) 111-22-33", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Номер с +7): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: некорректная длина)
    inp3 = "12345"
    res3 = format_phone_number(inp3)
    assert "Ошибка" in res3, f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - короткий номер): '{inp3}' -> '{res3}'")


def test_task_11() -> None:
    print("\n--- Тестирование Задания 11: Общий префикс слов ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "программа программист программирование"
    res1 = find_longest_common_prefix(inp1)
    assert res1 == "программ", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Короткий префикс)
    inp2 = "полет поле полив"
    res2 = find_longest_common_prefix(inp2)
    assert res2 == "пол", f"Ошибка: {res2}"
    print(f"[OK] Тест 2 (Префикс 'пол'): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: нет общего префикса)
    inp3 = "кот дом лес"
    res3 = find_longest_common_prefix(inp3)
    assert res3 == "Нет общего префикса", f"Ошибка: {res3}"
    print(f"[OK] Тест 3 (Граничный - нет префикса): '{inp3}' -> '{res3}'")


def test_task_12() -> None:
    print("\n--- Тестирование Задания 12: Статистика текста ---")
    
    # Тест 1 (Пример из задания)
    inp1 = "Python 3 — отличный язык!"
    stats1 = calculate_text_statistics(inp1)
    res1 = format_text_statistics(stats1)
    assert res1 == "Слов: 4; букв: 18; цифр: 1; знаков препинания: 2", f"Ошибка: {res1}"
    print(f"[OK] Тест 1 (Пример): '{inp1}' -> '{res1}'")
    
    # Тест 2 (Текст с различными знаками)
    inp2 = "Код 404: страница не найдена!"
    stats2 = calculate_text_statistics(inp2)
    res2 = format_text_statistics(stats2)
    # Слов: 5 ('Код', '404', 'страница', 'не', 'найдена')
    # Букв: 3 + 8 + 2 + 7 = 20
    # Цифр: 3 ('404')
    # Знаков: 2 (':' и '!')
    assert stats2 == {"words": 5, "letters": 20, "digits": 3, "punctuation": 2}, f"Ошибка: {stats2}"
    print(f"[OK] Тест 2 (Статистика): '{inp2}' -> '{res2}'")
    
    # Тест 3 (Граничный: пустая строка)
    inp3 = "     "
    stats3 = calculate_text_statistics(inp3)
    assert stats3 == {"words": 0, "letters": 0, "digits": 0, "punctuation": 0}, f"Ошибка: {stats3}"
    print(f"[OK] Тест 3 (Граничный - пустая строка): 0 слов, 0 букв, 0 цифр, 0 знаков")


def run_all_tests() -> None:
    print("=" * 60)
    print("      ЗАПУСК ТЕСТОВ ДЛЯ ВСЕХ 12 ЗАДАНИЙ ПО СТРОКАМ")
    print("=" * 60)
    test_task_01()
    test_task_02()
    test_task_03()
    test_task_04()
    test_task_05()
    test_task_06()
    test_task_07()
    test_task_08()
    test_task_09()
    test_task_10()
    test_task_11()
    test_task_12()
    print("\n" + "=" * 60)
    print("      ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ! (36/36 проверок)")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

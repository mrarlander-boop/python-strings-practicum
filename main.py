"""
Главный модуль для запуска практической работы "Задания по строкам в Python".
Позволяет запускать любое из 12 заданий в интерактивном режиме или протестировать всё сразу.
"""

import sys
from tasks.task_01_word_frequency import main as run_task_01
from tasks.task_02_most_frequent_char import main as run_task_02
from tasks.task_03_normalize_sentence import main as run_task_03
from tasks.task_04_remove_adjacent_duplicates import main as run_task_04
from tasks.task_05_check_email import main as run_task_05
from tasks.task_06_caesar_cipher import main as run_task_06
from tasks.task_07_sum_numbers_in_text import main as run_task_07
from tasks.task_08_alternate_case import main as run_task_08
from tasks.task_09_check_anagram import main as run_task_09
from tasks.task_10_format_phone_number import main as run_task_10
from tasks.task_11_longest_common_prefix import main as run_task_11
from tasks.task_12_text_statistics import main as run_task_12


TASK_RUNNERS = {
    "1": ("Подсчёт частоты слов", run_task_01),
    "2": ("Самый частый символ", run_task_02),
    "3": ("Нормализация предложения", run_task_03),
    "4": ("Удаление соседних повторов", run_task_04),
    "5": ("Проверка адреса электронной почты", run_task_05),
    "6": ("Шифр Цезаря", run_task_06),
    "7": ("Сумма чисел в тексте", run_task_07),
    "8": ("Чередование регистра", run_task_08),
    "9": ("Проверка анаграмм", run_task_09),
    "10": ("Форматирование номера телефона", run_task_10),
    "11": ("Общий префикс слов", run_task_11),
    "12": ("Статистика текста", run_task_12),
}


def print_menu() -> None:
    print("\n" + "=" * 55)
    print("      ПРАКТИЧЕСКАЯ РАБОТА: ЗАДАНИЯ ПО СТРОКАМ В PYTHON")
    print("=" * 55)
    for num, (title, _) in TASK_RUNNERS.items():
        print(f"  [{num:>2}] Задание {num}: {title}")
    print("  [ t] Запустить автоматические тесты (test_tasks.py)")
    print("  [ 0] Выход")
    print("=" * 55)


def main() -> None:
    while True:
        print_menu()
        choice = input("\nВыберите номер задания (или '0' для выхода): ").strip().lower()
        
        if choice == "0":
            print("\nЗавершение программы. До свидания!")
            break
        elif choice == "t":
            import test_tasks
            test_tasks.run_all_tests()
        elif choice in TASK_RUNNERS:
            title, runner = TASK_RUNNERS[choice]
            print(f"\n--- Запуск задания {choice}: {title} ---")
            try:
                runner()
            except Exception as e:
                print(f"Ошибка при выполнении задания: {e}")
            input("\nНажмите Enter, чтобы вернуться в главное меню...")
        else:
            print("Неверный выбор. Пожалуйста, укажите число от 1 до 12, 't' или '0'.")


if __name__ == "__main__":
    main()

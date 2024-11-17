# main.py

from banking import (
    withdraw,
    deposit,
    get_account_balance,
    read_account_data,
    transfer_funds,
    calculate_interest,
    update_account_limit,
    close_account,
    authenticate_user,
    open_new_account,
    change_password,
    apply_loan,
    get_accounts,
)


def main_function():
    """
    Шаг 9: Функция, которая последовательно вызывает все созданные ранее функции.
    """
    accounts = get_accounts()

    # Шаг 1: Функции, выбрасывающие исключения без их обработки
    print("\n--- Шаг 1: Функции без обработки исключений ---")
    try:
        print("Вклад 1000 на счет 12345:")
        deposit('12345', 1000)
        print("Новый баланс:", get_account_balance('12345'))
    except Exception as e:
        print(e)

    try:
        print("Снятие 500 со счета 67890:")
        withdraw('67890', 500)
        print("Новый баланс:", get_account_balance('67890'))
    except Exception as e:
        print(e)

    # Шаг 2: Функция с обработчиком общего типа исключений
    print("\n--- Шаг 2: Функция с общим обработчиком исключений ---")
    print("Получение баланса для счета 00000 (не существует):")
    balance = get_account_balance('00000')
    print("Баланс:", balance)

    # Шаг 3: Функция с обработчиком исключений и блоком finally
    print("\n--- Шаг 3: Функция с обработчиком исключений и блоком finally ---")
    print("Чтение данных счета для счета 12345:")
    data = read_account_data('12345')
    print("Данные счета:", data)

    # Шаг 4: Функции с несколькими обработчиками исключений
    print("\n--- Шаг 4: Функции с несколькими обработчиками исключений ---")
    print("Перевод 300 со счета 12345 на счет 67890:")
    transfer_funds('12345', '67890', 300)
    print("Новый баланс 12345:", get_account_balance('12345'))
    print("Новый баланс 67890:", get_account_balance('67890'))

    print("Расчет процентов для счета 67890 при ставке 0.05:")
    interest = calculate_interest('67890', 0.05)
    print("Проценты:", interest)

    print("Обновление лимита счета 12345 до 10000:")
    update_account_limit('12345', 10000)
    print("Новый лимит счета:", accounts['12345']['limit'])

    # Шаг 5: Функция, генерирующая и обрабатывающая исключения
    print("\n--- Шаг 5: Функция, генерирующая и обрабатывающая исключения ---")
    print("Закрытие счета 00000 (не существует):")
    close_account('00000')

    print("Закрытие счета 12345 (не удастся, если баланс не равен нулю):")
    close_account('12345')

    # Установка баланса в ноль для успешного закрытия счета
    accounts['12345']['balance'] = 0
    close_account('12345')

    # Шаг 7: Функция, выбрасывающая пользовательское исключение
    print("\n--- Шаг 7: Функция, выбрасывающая пользовательское исключение ---")
    print("Аутентификация пользователя для счета 67890:")
    authenticate_user('67890', 'password')
    print("Аутентификация пользователя с неверным паролем:")
    authenticate_user('67890', 'wrongpassword')

    # Шаг 8: Дополнительные функции, демонстрирующие работу исключений
    print("\n--- Шаг 8: Дополнительные функции ---")
    print("Открытие нового счета 54321 с начальным депозитом 500:")
    open_new_account('54321', 500)
    print("Данные нового счета:", accounts['54321'])

    print("Смена пароля для счета 67890:")
    change_password('67890', 'password', 'newpassword')

    print("Подача заявки на кредит для счета 67890:")
    apply_loan('67890', 2000)

    print("Подача заявки на кредит с превышением лимита:")
    apply_loan('67890', 10000)

    # Финальная проверка
    print("\n--- Финальное состояние счетов ---")
    print("Счета:", accounts)


if __name__ == "__main__":
    main_function()

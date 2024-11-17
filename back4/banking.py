# banking.py

from exceptions import (
    InsufficientFundsError,
    AccountNotFoundError,
    TransactionLimitError,
    InvalidCredentialsError,
)

# Глобальные словари для хранения информации о счетах и паролях
accounts = {
    '12345': {'balance': 1000, 'limit': 5000},
    '67890': {'balance': 2000, 'limit': 5000},
}

passwords = {
    '12345': 'password',
    '67890': 'password',
}


# Шаг 1: Функции, выбрасывающие исключения без их обработки

def withdraw(account_number, amount):
    """
    Шаг 1: Функция, которая выбрасывает исключение при недостатке средств.
    """
    if account_number not in accounts:
        raise AccountNotFoundError(f"Счет {account_number} не найден.")
    if amount > accounts[account_number]['balance']:
        raise InsufficientFundsError("Недостаточно средств для снятия.")
    accounts[account_number]['balance'] -= amount
    return accounts[account_number]['balance']


def deposit(account_number, amount):
    """
    Шаг 1: Функция, которая выбрасывает исключение при превышении лимита счета.
    """
    if account_number not in accounts:
        raise AccountNotFoundError(f"Счет {account_number} не найден.")
    if amount + accounts[account_number]['balance'] > accounts[account_number]['limit']:
        raise TransactionLimitError("Сумма вклада превышает лимит счета.")
    accounts[account_number]['balance'] += amount
    return accounts[account_number]['balance']


# Шаг 2: Функция с одним обработчиком общего типа исключений (Exception), без блока finally

def get_account_balance(account_number):
    """
    Шаг 2: Функция с обработчиком общего типа исключений.
    """
    try:
        balance = accounts[account_number]['balance']
        return balance
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Логика обработки исключения
        return None


# Шаг 3: Функция с обработчиком общего типа исключений (Exception) и блоком finally

def read_account_data(account_number):
    """
    Шаг 3: Функция с обработчиком общего типа исключений и блоком finally.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        # Дополнительная логика чтения данных счета
        return accounts[account_number]
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Логика обработки исключения
        return None
    finally:
        # Логика для нормального завершения работы функции
        print("Завершено чтение данных счета.")


# Шаг 4: Функции с несколькими обработчиками разных типов исключений

def transfer_funds(from_account, to_account, amount):
    """
    Шаг 4: Функция с обработчиками нескольких типов исключений.
    """
    try:
        if from_account not in accounts:
            raise AccountNotFoundError(f"Счет отправителя {from_account} не найден.")
        if to_account not in accounts:
            raise AccountNotFoundError(f"Счет получателя {to_account} не найден.")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной.")
        if accounts[from_account]['balance'] < amount:
            raise InsufficientFundsError("Недостаточно средств для перевода.")
        # Выполнение перевода
        accounts[from_account]['balance'] -= amount
        accounts[to_account]['balance'] += amount
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
        # Логика обработки AccountNotFoundError
    except InsufficientFundsError as e:
        print(f"Ошибка средств: {e}")
        # Логика обработки InsufficientFundsError
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        # Логика обработки ValueError
    finally:
        # Логика для нормального завершения работы функции
        print("Попытка перевода завершена.")


def calculate_interest(account_number, rate):
    """
    Шаг 4: Функция с обработчиками нескольких типов исключений.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if not isinstance(rate, (int, float)):
            raise TypeError("Процентная ставка должна быть числом.")
        if rate < 0:
            raise ValueError("Процентная ставка не может быть отрицательной.")
        interest = accounts[account_number]['balance'] * rate
        return interest
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    finally:
        print("Расчет процентов завершен.")


def update_account_limit(account_number, new_limit):
    """
    Шаг 4: Функция с обработчиками нескольких типов исключений.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if not isinstance(new_limit, (int, float)):
            raise TypeError("Новый лимит должен быть числом.")
        if new_limit < 0:
            raise ValueError("Новый лимит не может быть отрицательным.")
        accounts[account_number]['limit'] = new_limit
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    finally:
        print("Обновление лимита счета завершено.")


# Шаг 5: Функция, генерирующая исключения с помощью raise и обрабатывающая их

def close_account(account_number):
    """
    Шаг 5: Функция, генерирующая исключения с помощью raise и обрабатывающая их.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if accounts[account_number]['balance'] != 0:
            raise Exception("Баланс счета не равен нулю. Невозможно закрыть счет.")
        # Закрытие счета
        del accounts[account_number]
        print(f"Счет {account_number} успешно закрыт.")
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Процесс закрытия счета завершен.")


# Шаг 7: Функция, выбрасывающая пользовательское исключение и обрабатывающая его

def authenticate_user(account_number, password):
    """
    Шаг 7: Функция, выбрасывающая пользовательское исключение и обрабатывающая его.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if passwords.get(account_number) != password:
            raise InvalidCredentialsError("Неверный пароль.")
        print("Аутентификация успешна.")
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except InvalidCredentialsError as e:
        print(f"Ошибка аутентификации: {e}")
    finally:
        print("Попытка аутентификации завершена.")


# Шаг 8: Дополнительные функции, демонстрирующие работу исключений

def open_new_account(account_number, initial_deposit):
    """
    Шаг 8: Функция, демонстрирующая исключение при создании уже существующего счета.
    """
    try:
        if account_number in accounts:
            raise Exception("Счет уже существует.")
        if initial_deposit < 0:
            raise ValueError("Начальный депозит не может быть отрицательным.")
        accounts[account_number] = {'balance': initial_deposit, 'limit': 5000}
        passwords[account_number] = 'password'  # Пароль по умолчанию
        print(f"Счет {account_number} успешно открыт.")
    except Exception as e:
        print(f"Ошибка: {e}")


def change_password(account_number, old_password, new_password):
    """
    Шаг 8: Функция, демонстрирующая исключение при смене пароля.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if passwords.get(account_number) != old_password:
            raise InvalidCredentialsError("Неверный старый пароль.")
        passwords[account_number] = new_password
        print("Пароль успешно изменен.")
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except InvalidCredentialsError as e:
        print(f"Ошибка аутентификации: {e}")
    finally:
        print("Попытка смены пароля завершена.")


def apply_loan(account_number, loan_amount):
    """
    Шаг 8: Функция, демонстрирующая исключение при подаче заявки на кредит.
    """
    try:
        if account_number not in accounts:
            raise AccountNotFoundError(f"Счет {account_number} не найден.")
        if loan_amount <= 0:
            raise ValueError("Сумма кредита должна быть положительной.")
        # Простая логика одобрения кредита
        if loan_amount > accounts[account_number]['balance'] * 2:
            raise Exception("Сумма кредита превышает допустимый лимит.")
        print(f"Кредит на сумму {loan_amount} одобрен для счета {account_number}.")
    except AccountNotFoundError as e:
        print(f"Ошибка счета: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except Exception as e:
        print(f"Ошибка при одобрении кредита: {e}")
    finally:
        print("Процесс подачи заявки на кредит завершен.")


# Вспомогательные функции для доступа к словарям accounts и passwords

def get_accounts():
    """
    Функция для получения словаря счетов.
    """
    return accounts


def get_passwords():
    """
    Функция для получения словаря паролей.
    """
    return passwords

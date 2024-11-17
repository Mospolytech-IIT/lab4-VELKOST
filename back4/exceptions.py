# exceptions.py

# Шаг 6: Пользовательские исключения

class InsufficientFundsError(Exception):
    """Вызывается, когда на счете недостаточно средств для транзакции."""
    pass


class AccountNotFoundError(Exception):
    """Вызывается, когда указанный номер счета не существует."""
    pass


class TransactionLimitError(Exception):
    """Вызывается, когда сумма транзакции превышает установленный лимит."""
    pass


class InvalidCredentialsError(Exception):
    """Вызывается при неверных учетных данных для аутентификации."""
    pass

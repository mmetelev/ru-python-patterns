class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def register_user(self, username, password):
        user = User(username, password)
        # Логика регистрации нового пользователя
        # Другие действия при регистрации

    def authenticate_user(self, username, password):
        pass
        # Логика аутентификации пользователя
        # Проверка имени пользователя и пароля
        # Возвращение True, если аутентификация успешна, иначе False

    def reset_password(self, username, new_password):
        pass
        # Логика сброса пароля пользователя
        # Обновление пароля пользователя в базе данных
        # Отправка уведомления пользователю о смене пароля

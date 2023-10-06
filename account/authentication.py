from django.contrib.auth.models import User

class EmailAuthBackend:
    # 
    # Аутентифицировать посредством адреса электронной почты
    #

    # authenticate() - извлекается пользователь с данным мэйлом, пароль проверяется через check_password() (сравнивает хеши)
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None 
        
        # Отлавливаем ошибку, если найдено несколько пользователей на один мейл или пользователь с таким мейлом не найден
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        

    # Пользователь извлекается по id
    def get_user(self, user_id):
        try:
            # pk - primary key. Так как по умолчанию id - первичный ключ, ищем поле по нему
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
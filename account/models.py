from django.db import models
from django.conf import settings

# Класс - расширение модели User, которая содержит связи один-к-одному со встроенной джанго моделью User и любые дополнительные поля
# В данном случае профиль будет содержать дату рождения пользователя и его фотографию 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    # photo - экземпляр класса ImageField (поле опционально т.к. blank=True)
    # upload_to - место для сохранения медиафайлов
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    

    def __str__(self):
        return f'Profile of {self.user.username}'
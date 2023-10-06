from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    # Добавлены поля для установки пароля
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    
    # Здесь была создана модельная форма для модели пользователя
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


    # Метод для проверки (по типу введите пароль еще раз) - если не совпадает, вызываем ошибку валидации
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

    # Метод предотвращает создание двух пользователей с одинаковым мэйлом
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    

# Позволяет редактировать свое имя, фамилию, почтовый адрес (встроенные атрибуты модели User)
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # Теперь пользователь не сможет отредактировать свой email на уже зарегистрированный
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data


# Позволяет пользователям редактировать данные профиля, сохраненные в конкретно-прикладной модели Profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

from django import forms
from django.contrib.auth.models import User


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
    

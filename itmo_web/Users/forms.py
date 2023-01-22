from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=(u'Имя пользователя'), widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input is-rounded'}))
    first_name = forms.CharField(max_length=50, label=(u'Фамилия'), required=True, widget=forms.TextInput(
        attrs={'placeholder': ('Фамилия')}))
    last_name = forms.CharField(max_length=50, required=True, label=(u'Имя'),
                                widget=forms.TextInput(attrs={'placeholder': ('Имя')}))
    password1 = forms.CharField(label=(u'Пароль'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=(u'Пароль еще раз'),
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ['rating']
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label=(u'Фамилия'), required=True, widget=forms.TextInput(
        attrs={'placeholder': ('Фамилия'), 'class': 'input is-rounded'}))
    last_name = forms.CharField(max_length=50, required=True, label=(u'Имя'),
                                widget=forms.TextInput(attrs={'placeholder': ('Имя'), 'class': 'input is-rounded'}))

    class Meta:
        model = User
        exclude = ['username', 'rating']
        fields = ['last_name', 'first_name']


class ProfileUpdateForm(forms.ModelForm):
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'input is-rounded'}))

    class Meta:
        model = Profile
        exclude = ['user', 'rating']
        field = ('phonenumber')


class LoginForm(forms.ModelForm):
    username = forms.CharField(label=(u'Имя пользователя'))
    password = forms.CharField(label=(u'Пароль'))

    class Meta:
        model = User
        fields = ('username', 'password')


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label=(u'Имя пользователя'),
                               widget=forms.TextInput(attrs={'class': 'input is-rounded'}))
    password = forms.CharField(label=(u"Пароль"), widget=forms.PasswordInput(attrs={'class': 'input is-rounded'}))

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Вы вели данные неправильно'
        super().__init__(*args, **kwargs)


class ProfileRegisterForm(forms.ModelForm):
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'input is-rounded'}))

    class Meta:
        model = Profile
        fields = ['phonenumber']
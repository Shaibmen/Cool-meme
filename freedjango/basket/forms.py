from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from shop.models import Order
from django.contrib.auth.models import User



class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, required=True, label='кол-во', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_firstname',
            'buyer_secondname',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type'
        )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Логин пользователя",
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.CharField(
        label="Электронная почта пользователя",
        min_length=2,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Придумайте пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин пользователя",
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # password1 = forms.CharField(
    #     label="Ваш пароль",
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'})
    # )
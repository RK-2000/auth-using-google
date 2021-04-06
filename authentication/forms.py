from django import forms


class NewUserForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class LoginUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

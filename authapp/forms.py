from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import CorpUser
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CorpUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserEditForm(UserChangeForm):
    class Meta:
        model = CorpUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #     if data < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")
    #
    #     return data


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CorpUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'birthday', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            field.help_text = ''

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #     if data < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")
    #
    #     return data

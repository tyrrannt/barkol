from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import Person


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Person
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserEditForm(UserChangeForm):
    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday', 'password', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-4'
            field.help_text = ''


class UserProfileForm(UserChangeForm):
    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'surname', 'access_right', 'address', 'type_users', 'phone', 'email', 'birthday', 'password', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

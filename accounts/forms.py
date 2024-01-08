from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})
    #     self.fields['first_name'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
    #     self.fields['age'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
        self.fields['email'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
        self.fields['age'].widget.attrs.update({'class': 'form-control rounded-0 mb-3 mt-1'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control rounded-0 mb-1 mt-1'})

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

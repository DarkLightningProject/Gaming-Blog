from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
     class Meta:
       model = User
       fields = ['username','email']
    
     def __init__(self, *args: Any, **kwargs: Any):
        super(UserUpdateForm,self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', ]:
            self.fields[fieldname].help_text = None



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
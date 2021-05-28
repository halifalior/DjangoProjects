from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address','age']
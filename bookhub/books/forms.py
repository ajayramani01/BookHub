from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Recommendation

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['title', 'author', 'description','rating', 'genre', 'publication_date']
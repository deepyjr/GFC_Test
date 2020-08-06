from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class avec le modele article pour ajout et modifications
class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        
# class pour l'enregistrement d'un nouvel user
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
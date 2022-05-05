from django import forms
from django.contrib.auth.models import User

from OkangaShopApp.models import Okanga
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Okanga

        fields = ['item_title', 'item_description', 'item_image', 'item_amount', 'initial_item_amount']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

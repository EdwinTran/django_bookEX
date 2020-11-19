from django.forms import ModelForm
from .models import Book, RequestBook
from .models import Review
from django import forms

# Importing UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RequestBookForm(ModelForm):
    class Meta:
        model = RequestBook
        fields = [
           'name',
            'bookName',
            'email'
        ]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'title',
            'description',
        ]


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-Mail')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
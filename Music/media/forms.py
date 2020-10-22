from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Album, Song


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class AlbumForm(forms.ModelForm):
    created_date = forms.DateField()

    class Meta:
        model = Album
        fields = ('artist', 'album_name', 'genre', 'created_date','cover')

        widgets = {
            'cover':forms.ImageField(),
            'artist': forms.TextInput(),
            'album_name': forms.TextInput(),
            'genre': forms.TextInput()
        }


class SongForm(forms.ModelForm):
    song_name = forms.CharField(max_length=40)
    created_date = forms.DateField()
    album = forms.TextInput()

    class Meta:
        model = Song
        fields = ('album', 'song_name', 'created_date')

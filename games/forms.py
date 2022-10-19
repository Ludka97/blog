from django import forms


class GameForm(forms.Form):
    title = forms.CharField(max_length=50)
    release_data = forms.DateField()
    genre = forms.CharField(max_length=100)
    platform = forms.CharField(max_length=20)
    progress = forms.IntegerField()
    comment = forms.CharField(max_length=100)

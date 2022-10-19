from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField()
    text = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
    author = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    slug = forms.CharField(max_length=255)
    text = forms.CharField(max_length=255)

from django import forms

class NewsForm(forms.Form):
    title = forms.CharField(label='Title',max_length=50)
    content = forms.CharField(max_length=2000, widget=forms.Textarea(attrs = {'placeholder' : "write the content"}))
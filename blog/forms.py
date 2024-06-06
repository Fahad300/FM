from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control col-6',
            'placeholder': 'Enter your name'
        })
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control col-6',  
            'placeholder': 'Enter your email'
        })
    )
    comment = forms.CharField(
        max_length=300,
        required=True,
        label="Your Comment",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'form-control',  
            'placeholder': 'Enter your comment'
        })
    )
from django import forms

class BookrankForm(forms.Form):
    rank = forms.IntegerField(
        max_value=5,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "1-5"
        })
    )
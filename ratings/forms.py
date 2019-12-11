from django import forms

class RateForm(forms.Form):
    CHOICES = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    rating = forms.ChoiceField(
        choices=CHOICES,
    )
    notes = forms.CharField(max_length=120)
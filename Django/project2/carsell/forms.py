from django import forms

class CarSelectForm(forms.Form):
    MAKES = (
        ('volvo','Volvo'),
        ('saab','Saab'),
        ('fiat','Fiat'), 
        ('audi','Audi'), 
        )
    make = forms.ChoiceField(required=True, choices=MAKES)

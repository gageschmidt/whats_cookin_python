from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(
        label='Recipe Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'name', 'required': 'true'}
        )
    )
    ingredients = forms.CharField(
        label='Ingredients',
        widget=forms.Textarea(
            attrs={'class': 'ingredients', 'required': 'true'}
        )
    )
    directions = forms.CharField(
        label='Directions',
        widget=forms.Textarea(
            attrs={'class': 'directions', 'required': 'true'}
        )
    )

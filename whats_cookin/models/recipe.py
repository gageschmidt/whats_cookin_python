from django import forms


class RecipeForm(forms.Form):
    recipe_name = forms.CharField(
        label='Recipe Name',
        max_length=100,
    )

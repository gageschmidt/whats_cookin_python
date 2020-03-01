from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(
        label='Recipe Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'name-form-input', 'required': 'true'}
        )
    )
    ingredients = forms.CharField(
        label='Ingredients',
        widget=forms.Textarea(
            attrs={'class': 'ingredients-form-input', 'required': 'true'}
        )
    )
    directions = forms.CharField(
        label='Directions',
        widget=forms.Textarea(
            attrs={'class': 'directions-form-input', 'required': 'true'}
        )
    )

    class Media:
        css: {
            'all': ('submission.css',)
        }


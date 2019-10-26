from django.shortcuts import render

def index(request):
    return render(request, 'recipe_submission.html')
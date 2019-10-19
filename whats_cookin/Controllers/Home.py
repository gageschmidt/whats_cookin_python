from django.shortcuts import render


def index(self):
    return render(self, 'home.html', locals())

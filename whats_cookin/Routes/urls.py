from django.contrib import admin
from django.urls import path
from whats_cookin.Controllers import home
from whats_cookin.Controllers import recipe_submission
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('submitrecipe', recipe_submission.index, name='submitrecipe')
]

urlpatterns += staticfiles_urlpatterns()

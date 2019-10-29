from django.contrib import admin
from django.urls import path
from whats_cookin.controllers import home
from whats_cookin.controllers import submission
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('submit', submission.index, name='submit')
]

urlpatterns += staticfiles_urlpatterns()

from django.urls import path
from .views import home_view

app_name = 'Recipes'

urlpatterns = [
    path('', home_view, name='home'),
]

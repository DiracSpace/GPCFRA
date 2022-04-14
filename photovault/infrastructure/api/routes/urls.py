from django.conf.urls import include
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('', include(f'{settings.API_ROUTES}.hello_world.urls'))
]
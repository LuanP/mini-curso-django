from django.conf.urls import url
from participantes.views import olamundo

urlpatterns = [
    url(r'^olamundo$', olamundo),
]

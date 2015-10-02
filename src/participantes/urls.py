from django.conf.urls import url
from participantes.views import lista_participantes

urlpatterns = [
    url(r'^lista_participantes/$', lista_participantes),
]

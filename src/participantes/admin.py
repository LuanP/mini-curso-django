from django.contrib import admin
from participantes.models import Participante

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo')

from django.shortcuts import render
from participantes.models import Participante


def lista_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'list.html', {'participantes': participantes})

from django.db import models

class Participante(models.Model):
    GENDER_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=8, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.nome

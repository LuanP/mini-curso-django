# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='matricula',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nascimento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Masculino'), (b'F', b'Feminino')]),
        ),
    ]

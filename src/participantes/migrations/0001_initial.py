# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('matricula', models.CharField(max_length=8)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('foto', models.ImageField(upload_to=b'')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

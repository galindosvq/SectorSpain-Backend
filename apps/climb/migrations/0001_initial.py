# Generated by Django 2.2.5 on 2019-11-19 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_utils.choices
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('latitude', models.CharField(blank=True, max_length=45, null=True)),
                ('longitude', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(max_length=45)),
                ('province', models.CharField(choices=[('Alava', django_utils.choices.Choice('Alava', 'Álava')), ('Albacete', django_utils.choices.Choice('Albacete', 'Albacete')), ('Alicante', django_utils.choices.Choice('Alicante', 'Alicante')), ('Almeria', django_utils.choices.Choice('Almeria', 'Almería')), ('Asturias', django_utils.choices.Choice('Asturias', 'Asturias')), ('Avila', django_utils.choices.Choice('Avila', 'Ávila')), ('Badajoz', django_utils.choices.Choice('Badajoz', 'Badajoz')), ('Baleares', django_utils.choices.Choice('Baleares', 'Baleares')), ('Barcelona', django_utils.choices.Choice('Barcelona', 'Barcelona')), ('Burgos', django_utils.choices.Choice('Burgos', 'Burgos')), ('Caceres', django_utils.choices.Choice('Caceres', 'Cáceres')), ('Cadiz', django_utils.choices.Choice('Cadiz', 'Cádiz')), ('Cantabria', django_utils.choices.Choice('Cantabria', 'Cantabria')), ('Castellon', django_utils.choices.Choice('Castellon', 'Castellón')), ('Ceuta', django_utils.choices.Choice('Ceuta', 'Ceuta')), ('Ciudad Real', django_utils.choices.Choice('Ciudad Real', 'Ciudad Real')), ('Cordoba', django_utils.choices.Choice('Cordoba', 'Córdoba')), ('Coruña', django_utils.choices.Choice('Coruña', 'Coruña, A')), ('Cuenca', django_utils.choices.Choice('Cuenca', 'Cuenca')), ('Gipuzcoa', django_utils.choices.Choice('Gipuzcoa', 'Guipúzcoa')), ('Gerona', django_utils.choices.Choice('Gerona', 'Gerona')), ('Granada', django_utils.choices.Choice('Granada', 'Granada')), ('Guadalajara', django_utils.choices.Choice('Guadalajara', 'Guadalajara')), ('Huelva', django_utils.choices.Choice('Huelva', 'Huelva')), ('Huesca', django_utils.choices.Choice('Huesca', 'Huesca')), ('Jaen', django_utils.choices.Choice('Jaen', 'Jaén')), ('Leon', django_utils.choices.Choice('Leon', 'León')), ('Lerida', django_utils.choices.Choice('Lerida', 'Lérida')), ('Lugo', django_utils.choices.Choice('Lugo', 'Lugo')), ('Madrid', django_utils.choices.Choice('Madrid', 'Madrid')), ('Malaga', django_utils.choices.Choice('Malaga', 'Málaga')), ('Melilla', django_utils.choices.Choice('Melilla', 'Melilla')), ('Murcia', django_utils.choices.Choice('Murcia', 'Murcia')), ('Navarra', django_utils.choices.Choice('Navarra', 'Navarra')), ('Orense', django_utils.choices.Choice('Orense', 'Orense')), ('Palencia', django_utils.choices.Choice('Palencia', 'Palencia')), ('Palmas', django_utils.choices.Choice('Palmas', 'Palmas, Las')), ('Pontevedra', django_utils.choices.Choice('Pontevedra', 'Pontevedra')), ('Rioja', django_utils.choices.Choice('Rioja', 'Rioja, La')), ('Salamanca', django_utils.choices.Choice('Salamanca', 'Salamanca')), ('Segovia', django_utils.choices.Choice('Segovia', 'Segovia')), ('Sevilla', django_utils.choices.Choice('Sevilla', 'Sevilla')), ('Soria', django_utils.choices.Choice('Soria', 'Soria')), ('Tarragona', django_utils.choices.Choice('Tarragona', 'Tarragona')), ('Tenerife', django_utils.choices.Choice('Tenerife', 'Santa Cruz de Tenerife')), ('Teruel', django_utils.choices.Choice('Teruel', 'Teruel')), ('Toledo', django_utils.choices.Choice('Toledo', 'Toledo')), ('Valencia', django_utils.choices.Choice('Valencia', 'Valencia')), ('Valladolid', django_utils.choices.Choice('Valladolid', 'Valladolid')), ('Vizcaya', django_utils.choices.Choice('Vizcaya', 'Vizcaya')), ('Zamora', django_utils.choices.Choice('Zamora', 'Zamora')), ('Zaragoza', django_utils.choices.Choice('Zaragoza', 'Zaragoza'))], max_length=25)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('parking_coordinates', models.CharField(blank=True, max_length=45)),
                ('latitude', models.CharField(blank=True, max_length=45, null=True)),
                ('longitude', models.CharField(blank=True, max_length=45, null=True)),
                ('orientation', models.CharField(blank=True, choices=[('N', 'NORTE'), ('NE', 'NORESTE'), ('E', 'ESTE'), ('SE', 'SURESTE'), ('S', 'SUR'), ('SO', 'SUROESTE'), ('O', 'OESTE'), ('NO', 'NOROESTE')], max_length=2)),
                ('picture', models.FileField(blank=True, null=True, upload_to='media/')),
                ('approach', models.TextField(blank=True)),
                ('rope', models.IntegerField(blank=True, null=True)),
                ('warning', models.BooleanField(blank=True, default=False)),
                ('warning_text', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('rock_type', models.CharField(blank=True, max_length=45)),
                ('crag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climb.Crag')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True)),
                ('grade', models.CharField(choices=[('?', '?'), ('5', '5'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b'), ('8b+', '8b+'), ('8c', '8c'), ('8c+', '8c+'), ('9a', '9a'), ('9a+', '9a+'), ('9b', '9b'), ('9b+', '9b+'), ('9c', '9c')], max_length=10)),
                ('rating', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('nanchor', models.IntegerField(blank=True, null=True)),
                ('anchor_type', models.CharField(blank=True, max_length=15)),
                ('lowering_station', models.CharField(blank=True, max_length=20)),
                ('pith', models.IntegerField(blank=True, null=True)),
                ('feature', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climb.Sector')),
            ],
        ),
    ]

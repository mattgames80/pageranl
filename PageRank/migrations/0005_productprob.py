# Generated by Django 5.0.4 on 2024-04-19 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarritoApp', '0002_producto_descripcion_producto_imagen'),
        ('PageRank', '0004_userviewcount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prob', models.FloatField(default=0)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarritoApp.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

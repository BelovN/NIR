# Generated by Django 2.2.17 on 2021-03-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('IAGA', models.CharField(max_length=150, verbose_name='Краткое название')),
                ('lat', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Широта')),
                ('lon', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Долгота')),
                ('mlat', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Магнитная широта')),
                ('mlon', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Магнитная долгота')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станции',
            },
        ),
    ]

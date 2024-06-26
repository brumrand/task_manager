# Generated by Django 5.0.4 on 2024-04-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Personal', 'Personal'), ('Trabajo', 'Trabajo'), ('Estudio', 'Estudio'), ('Otros', 'Otros')], max_length=20)),
                ('deadline', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

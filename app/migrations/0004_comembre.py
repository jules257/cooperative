# Generated by Django 4.1.7 on 2023-02-21 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cooperative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comembre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entree', models.DateField()),
                ('cooperative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cooperative')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.membre')),
            ],
        ),
    ]

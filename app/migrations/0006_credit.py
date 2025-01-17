# Generated by Django 4.1.7 on 2023-02-21 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cotisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_obtention', models.DateField()),
                ('montant_credit', models.IntegerField()),
                ('date_payement', models.DateField()),
                ('taux', models.FloatField()),
                ('cooperative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cooperative')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.membre')),
            ],
        ),
    ]

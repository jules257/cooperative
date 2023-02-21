# Generated by Django 4.1.7 on 2023-02-21 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_membre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cooperative', models.CharField(max_length=45)),
                ('adresse', models.CharField(max_length=45)),
                ('localisation', models.CharField(max_length=45)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
                ('membre', models.ManyToManyField(blank=True, to='app.membre')),
            ],
        ),
    ]
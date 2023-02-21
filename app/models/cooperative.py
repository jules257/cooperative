from django.db import models
from app.models import Categorie


class Cooperative(models.Model):
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    nom_cooperative = models.CharField(max_length=45)
    adresse = models.CharField(max_length=45)
    localisation = models.CharField(max_length=45)
    membre = models.ManyToManyField('Membre' ,blank = True)
    
    
  
    
    
    
    
    
    def __str__(self):
        return self.nom_cooperative
from django.db import models
from app.models import Cooperative , Membre


class Comembre(models.Model):
    cooperative = models.ForeignKey(Cooperative,on_delete=models.CASCADE)
    
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    date_entree = models.DateField()
   
    
    
  
    
    
    
    
    
    def __str__(self):
        return self.cooperative.nom_cooperative+ "  " +self.membre.nom_membre+ " " +self.membre.prenom_membre
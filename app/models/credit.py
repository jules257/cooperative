from django.db import models
from app.models import Cooperative,Membre


class Credit(models.Model):
    cooperative = models.ForeignKey(Cooperative,on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    
  
    
    date_obtention = models.DateField()
    montant_credit = models.IntegerField()
    date_payement = models.DateField()
    taux = models.FloatField()
    
    

    
    
  
    
    
    
    
    
    def __str__(self):
        return self.cooperative.nom_cooperative+ " " +self.membre.nom_membre+ " " +self.membre.prenom_membre
from django.db import models
from app.models import Cooperative,Membre
MOTIF = (('Sociale', 'sociale'), ('Epargne', 'epargne'))


class Cotisation(models.Model):
    
     cooperative = models.ForeignKey(Cooperative,on_delete=models.CASCADE)
     membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
     

     date_cotisation = models.DateField()

     montant_paye = models.IntegerField()
     motif = models.CharField(choices= MOTIF,max_length=62)

     
     
     
     def __str__(self):
         return self.cooperative.nom_cooperative+ " " +self.membre.nom_membre+ " " +self.membre.prenom_membre
         
     
     
     
  
     
  
  
    
    
    
    
    
   
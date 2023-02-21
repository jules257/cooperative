from django.db import models
from app.models import Credit


class Remboursement(models.Model):
    
     credit = models.ForeignKey(Credit,on_delete=models.CASCADE)
     date_remboursement = models.DateField()
     montant_remboursement = models.IntegerField()
     reste_credit = models.IntegerField()
     
     
     
     def __str__(self):
          return self.credit.cooperative.nom_cooperative+ " " +self.credit.membre.nom_membre+ " " +self.credit.membre.prenom_membre+ " " +self.credit.montant_credit
    
from django.db import models
SEXE = (('Masculin', 'masculin'), ('Feminin', 'feminin'))
ETAT = (('Actif', 'actif'), ('Non actif', 'non actif'))



class Membre(models.Model):
    nom_membre = models.CharField(max_length=45)
    prenom_membre = models.CharField(max_length=45)
    datenaissance = models.DateField()
    sexe = models.CharField(choices=SEXE, max_length=45)
    telephone = models.CharField(max_length=45)
    image=models.ImageField(upload_to='media', blank=True, null=True)
    adresse = models.CharField(max_length=45)
    nationalite = models.CharField(max_length=45)
    etat = models.CharField( choices=ETAT,max_length=45)
    
    
    def __str__(self):
        return self.nom_membre+ " " +self.prenom_membre
    
    
    
    
    
    
    
  
    
    
    
    
    

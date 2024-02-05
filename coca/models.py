from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class InformationsInternaute(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    addres = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)

    # Ajoutez d'autres champs au besoin

    def __str__(self):
        return self.nom

# Panneau Model
class Panneau(models.Model):

    nom = models.CharField(max_length=50)
    PV = models.IntegerField() #in Wp
    R_load = models.IntegerField() # in W
    M_load = models.IntegerField() # in W
    cote = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("Panneau_detail", kwargs={"pk": self.pk})

#Types  de Panneau Model
class TypePanneau(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TypePanneau'
        verbose_name_plural = 'TypePanneaus'

#TYpePanneau Relationnal ** Model

class Type_Panneau(models.Model):
    panneau = models.ForeignKey("Panneau", on_delete=models.CASCADE, related_name="types")
    type = models.ForeignKey("TypePanneau", on_delete=models.CASCADE)
    prix = models.IntegerField()
    def __str__(self):
        return str(self.panneau) + str(self.type)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Type_Panneau'
        verbose_name_plural = 'Type_Panneaus'
# Appareils Model
class Appareil(models.Model):
    nom = models.CharField(max_length=50)
    type =  models.CharField(max_length=50, blank=True)
    cote = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nom + "(" + str(self.cote) + ")"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Appareil'
        verbose_name_plural = 'Appareils'
# Devis Model
class Devis(models.Model):
    internaute_temp = models.ForeignKey(InformationsInternaute, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    appliances = []
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devis'
        verbose_name_plural = 'Deviss'
#Appareil_devis Model
class Devis_Appareil(models.Model):
    appareil  = models.ForeignKey("Appareil", on_delete=models.CASCADE)
    devis  = models.ForeignKey("Devis", on_delete=models.CASCADE)
    quantite = models.IntegerField()
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devis_Appareil'
        verbose_name_plural = 'Devis_Appareils'
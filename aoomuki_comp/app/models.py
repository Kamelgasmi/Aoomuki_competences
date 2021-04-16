from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Statut(models.Model):
    name = models.CharField('nom',max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Statut"

# class User(models.Model):
#     Lastname = models.CharField('nom',max_length=200, unique=True)
#     Firstname = models.CharField('prénom',max_length=200, unique=True)
#     statut = models.ForeignKey(Statut,on_delete=models.CASCADE, null=True)
#     login = models.CharField('login',max_length=200, unique=True)
#     password = models.CharField(max_length=50)
#     def __str__(self):
#         return self.Lastname + " " + self.Firstname
#     class Meta:
#         verbose_name = "Utilisateur"

class Society(models.Model):
    name = models.CharField('Société', max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Société"

class ListCertification(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Certification"


class Field(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    description = models.CharField('description', max_length=250, unique=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Domaine"

class ListLevel(models.Model):
    value = models.CharField('valeur', max_length=10, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    def __str__(self):
        return self.value
    class Meta:
        verbose_name = "Liste des niveaux"

class ListInterest(models.Model):
    value = models.CharField('valeur', max_length=10, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    def __str__(self):
        return self.value
    class Meta:
        verbose_name = "Liste des intérêt"
        
class Competence(models.Model):
    name = models.CharField('nom', max_length=50, unique=False)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    field = models.ForeignKey(Field,on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Compétence"

class ListWorkStation(models.Model):
    name = models.CharField('nom', max_length=50, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Liste postes de travail"

class Collaborater(models.Model):
    collaborater = models.BooleanField('Etes-vous un collaborateur ?',default=True)
    user = models.OneToOneField(User, verbose_name="Utilisateur ", on_delete=models.CASCADE, null=True, blank=True, unique=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Collaborateur"

class UserProfil(models.Model):
    Extern = models.BooleanField('Externe à l\'entreprise?',default=False)
    society = models.ForeignKey(Society,verbose_name="Société", on_delete=models.CASCADE, null=True)
    workstation = models.ForeignKey(ListWorkStation, verbose_name="Poste de travail", on_delete=models.CASCADE, null=True)
    certification = models.ManyToManyField(ListCertification, related_name='collaboraters', blank=True)
    user = models.ForeignKey(User, verbose_name="Utilisateur ", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Profil"


class ListofCompetence(models.Model):
    User = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE, null=True)
    Competence = models.ForeignKey(Competence,verbose_name="Compétence", on_delete=models.CASCADE, null=True)
    ListInterest = models.ForeignKey(ListInterest, verbose_name="Intérêt", on_delete=models.CASCADE, null=True, default=0)
    ListLevel = models.ForeignKey(ListLevel, verbose_name="Niveau", on_delete=models.CASCADE, null=True, default=0)

    def __str__(self):
        return self.Competence
    class Meta:
        verbose_name = "Competences des utilisateur"


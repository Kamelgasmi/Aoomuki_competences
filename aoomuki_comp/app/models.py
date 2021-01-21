from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Statut(models.Model):
    name = models.CharField('nom',max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Statut"

class User(models.Model):
    Lastname = models.CharField('nom',max_length=200, unique=True)
    Firstname = models.CharField('prénom',max_length=200, unique=True)
    statut = models.ForeignKey(Statut,on_delete=models.CASCADE, null=True)
    login = models.CharField('login',max_length=200, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.Lastname + " " + self.Firstname
    class Meta:
        verbose_name = "Utilisateurs"

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
        verbose_name = "Certifications"


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
        verbose_name = "Liste des intérêts"
        
class Competence(models.Model):
    name = models.CharField('nom', max_length=50, unique=False)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    field = models.ForeignKey(Field,on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Compétences"

class ListWorkStation(models.Model):
    name = models.CharField('nom', max_length=50, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Liste postes de travail"

class Collaborater(models.Model):
    Lastname = models.CharField('Nom',max_length=200, unique=True)
    Firstname = models.CharField('Prénom',max_length=200, unique=True)
    Extern = models.BooleanField('Externe ?',default=False)
    society = models.ForeignKey(Society,verbose_name="Société", on_delete=models.CASCADE, null=True)
    workstation = models.ForeignKey(ListWorkStation, verbose_name="Poste de travail", on_delete=models.CASCADE, null=True)
    certification = models.ManyToManyField(ListCertification, related_name='collaboraters', blank=True)
    statut = models.ForeignKey(Statut,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name="Utilisateur ", on_delete=models.CASCADE, null=True)
    # interest = models.ManyToManyField(ListInterest, related_name='collaboraters', blank=True)

    def __str__(self):
        return self.Lastname
    class Meta:
        verbose_name = "Collaborateurs"


class ListofCompetence(models.Model):
    Collaborater = models.ForeignKey(Collaborater,on_delete=models.CASCADE, null=True, default=1)
    Competence = models.ForeignKey(Competence,on_delete=models.CASCADE, null=True, default=1)
    ListInterest = models.ForeignKey(ListInterest, on_delete=models.CASCADE, null=True, default=1)
    ListLevel = models.ForeignKey(ListLevel,on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "ListCompetence"


# class CollaboraterCompetences(models.Model):

#     class Meta:
#         order_with_respect_to = 'collaborater'
#         unique_together = [
#             ('collaborater', 'competence'),
#         ]

#     LEVEL_CHOICES = [
#         (0, "Aucun"),
#         (1, "Des notions"),
#         (2, "Débutant"),
#         (3, "Intermédiaire"),
#         (4, "Confirmés"),
#     ]

#     collaborater = models.ForeignKey(Collaborater, models.CASCADE)
#     competence = models.ForeignKey(Competence, models.CASCADE)
#     level = models.CharField('valeur', max_length=10, unique=True,choices=LEVEL_CHOICES)



# class LinkCollaborateurCompetence(models.Model):
#     former = models.BooleanField('formateur ?',default=False)
#     collaborater = 
#     level = 
#     interest = 
#     competence = 
#     def __str__(self):
#         return self.collaborater
#     class Meta:
#         verbose_name = "liens collaborateurs / compétences"

###########################################################################################################################

# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.


# class Statut(models.Model):
#     name = models.CharField('nom',max_length=200, unique=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Statut"

# class User(models.Model):
#     Lastname = models.CharField('nom',max_length=200, unique=True)
#     Firstname = models.CharField('prénom',max_length=200, unique=True)
#     statut = models.ForeignKey(Statut,on_delete=models.CASCADE, null=True)
#     login = models.CharField('login',max_length=200, unique=True)
#     password = models.CharField(max_length=50)
#     def __str__(self):
#         return self.Lastname + " " + self.Firstname
#     class Meta:
#         verbose_name = "Utilisateurs"

# class Society(models.Model):
#     name = models.CharField('Société', max_length=200, unique=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Société"

# class ListCertification(models.Model):
#     name = models.CharField('nom', max_length=200, unique=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Certifications"


# class Field(models.Model):
#     name = models.CharField('nom', max_length=200, unique=True)
#     description = models.CharField('description', max_length=250, unique=False)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Domaine"

# # class ListLevel(models.Model):
# #     value = models.CharField('valeur', max_length=10, unique=True)
# #     commentary = models.CharField('commentaire', max_length=250, unique=False)
# #     def __str__(self):
# #         return self.value
# #     class Meta:
# #         verbose_name = "Liste des niveaux"

# # class ListInterest(models.Model):
# #     value = models.CharField('valeur', max_length=10, unique=True)
# #     commentary = models.CharField('commentaire', max_length=250, unique=False)
# #     def __str__(self):
# #         return self.value
# #     class Meta:
# #         verbose_name = "Liste des intérêts"
        
# class Competence(models.Model):
#     name = models.CharField('nom', max_length=50, unique=False)
#     commentary = models.CharField('commentaire', max_length=250, unique=False)
#     field = models.ForeignKey(Field,on_delete=models.CASCADE, null=True, default=1)

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Compétences"

# class ListWorkStation(models.Model):
#     name = models.CharField('nom', max_length=50, unique=True)
#     commentary = models.CharField('commentaire', max_length=250, unique=False)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Liste postes de travail"

# class Collaborater(models.Model):
#     Lastname = models.CharField('Nom',max_length=200, unique=True)
#     Firstname = models.CharField('Prénom',max_length=200, unique=True)
#     Extern = models.BooleanField('Externe ?',default=False)
#     society = models.ForeignKey(Society,verbose_name="Société", on_delete=models.CASCADE, null=True)
#     workstation = models.ForeignKey(ListWorkStation, verbose_name="Poste de travail", on_delete=models.CASCADE, null=True)
#     certification = models.ManyToManyField(ListCertification, related_name='collaboraters', blank=True)
#     statut = models.ForeignKey(Statut,on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(User, verbose_name="Utilisateur ", on_delete=models.CASCADE, null=True)
#     competences = models.ManyToManyField(Competence,through='ListofCompetence', related_name='collaboraters', blank=True)
#     # interest = models.ManyToManyField(ListInterest, related_name='collaboraters', blank=True)

#     def __str__(self):
#         return self.Lastname
#     class Meta:
#         verbose_name = "Collaborateurs"


# class ListofCompetence(models.Model):
#     INTEREST_CHOICES = [
#         (0, "Aucun"),
#         (1, "Des notions"),
#         (2, "Débutant"),
#         (3, "Intermédiaire"),
#         (4, "Confirmés"),
#     ]
#     LEVEL_CHOICES = [
#         (0, "Aucun"),
#         (1, "Des notions"),
#         (2, "Débutant"),
#         (3, "Intermédiaire"),
#         (4, "Confirmés"),
#     ]

#     Collaborater = models.ForeignKey(Collaborater,on_delete=models.CASCADE, null=True, default=1)
#     Competence = models.ForeignKey(Competence,on_delete=models.CASCADE, null=True, default=1)
#     interest = models.IntegerField(choices=INTEREST_CHOICES, default=0)
#     level = models.IntegerField(choices=LEVEL_CHOICES, default=0)

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "ListCompetence"
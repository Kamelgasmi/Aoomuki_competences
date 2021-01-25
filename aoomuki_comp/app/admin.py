from django.contrib import admin

# Register your models here.
from .models import User, Collaborater, Field, Competence, ListLevel, ListInterest, ListWorkStation, ListCertification, Statut, Society, ListofCompetence



@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    pass

@admin.register(Collaborater)
class CollaboraterAdmin(admin.ModelAdmin):
    search_fields = ['Lastname', 'Firstname']
    pass

class CompetenceInline(admin.TabularInline):
    model = Competence
    fieldsets = [
        (None, {'fields': ['name',]})
        ] # list columns

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    inlines = [CompetenceInline,] # list of bookings made by a contact

class CollaboraterInline(admin.TabularInline):
    model = Collaborater
    fieldsets = [
        (None, {'fields': ['Lastname', 'Firstname','Extern', 'society','workstation', 'statut',]})
        ] # list columns

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CollaboraterInline,] # list of bookings made by a contact

class ListofCompetenceInline(admin.TabularInline):
    model = ListofCompetence
    fieldsets = [
        (None, {'fields': ['Competence', 'ListLevel', 'ListInterest']})
        ] # list columns

@admin.register(ListLevel)
class ListLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(ListInterest)
class ListInterestAdmin(admin.ModelAdmin):
    pass

@admin.register(ListWorkStation)
class ListWorkStationAdmin(admin.ModelAdmin):
    pass

@admin.register(ListCertification)
class ListCertificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Statut)
class StatutAdmin(admin.ModelAdmin):
    pass

@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    pass

@admin.register(ListofCompetence)
class ListofCompetenceAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Field, Competence, ListWorkStation, ListCertification, Statut, Society, ListofCompetence, UserProfil, Collaborater
from django.contrib.auth.models import User

admin.site.site_header = 'Administration Matrice des compétences AOOMUKI'

@admin.register(UserProfil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'society','workstation','Extern' )
    search_fields = ['user__last_name']
    pass
#********************************************************************************************************************
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('field','name', )
    pass

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass

#********************************************************************************************************************
class ProfilInline(admin.TabularInline):
    model = UserProfil
    fieldsets = [
        (None, {'fields': ['Extern', 'society','workstation', 'user']})
        ] # list columns

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfilInline,] 
#********************************************************************************************************************
@admin.register(ListWorkStation)
class ListWorkStationAdmin(admin.ModelAdmin):
    pass

@admin.register(Collaborater)
class CollaboraterAdmin(admin.ModelAdmin):
    list_display = ('user','user_last_name','user_first_name', 'collaborater' )
    search_fields = ['user__last_name']
    def user_last_name(self, obj):
        return obj.user.last_name

    def user_first_name(self, obj):
        return obj.user.first_name

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

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    pass

@admin.register(ListofCompetence)
class ListofCompetenceAdmin(admin.ModelAdmin):
    list_display = ('User', 'Competence', 'ListLevel', 'ListInterest')
    search_fields = ['User__username']
    pass

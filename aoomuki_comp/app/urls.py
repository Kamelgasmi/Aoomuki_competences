from django.urls import path, re_path
from app import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app'

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('Enregistrement/', views.register, name='Enregistrement'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:login'), name='logout'),
    # path('Formulaire_Compétences_Collaborateur/', views.AllFormlist, name='Formulaire_Compétences_Collaborateur'),
    # path('Ajouter_un_utilisateur/collaborateur', views.AddCollaborater, name='Ajouter_un_utilisateur/collaborateur'),
    path('search/', views.search, name='search'),
    path('Liste_des_collaborateurs/', views.ListCollaboraters, name='Liste_des_collaborateurs'),
    path('Liste_des_utilisateurs/', views.ListUsers, name='Liste_des_utilisateurs'),
    path('Liste_des_domaines/', views.ListField, name='Liste_des_domaines'),
    path('Liste_des_compétences/', views.ListCompetence, name='Liste_des_compétences'),
    path('Liste_des_certifications/', views.ListOfCertification, name='Liste_des_certifications'),
    path('Liste_des_sociétés/', views.ListSociety, name='Liste_des_sociétés'),
    path('Ajouter_Domaines_Compétences/', views.AddFieldCompDegreeSociety, name='Ajouter_Domaines_Compétences'),
    path('Ajouter_un_collaborateur/', views.AddCollabForm, name='Ajouter_un_collaborateur'),
    path('GraphComp/', views.CompetencesGraph, name='GraphComp'),
    # re_path(r'^Profil/(?P<user_id>[0-9]+)/$', views.ProfilsAdmin, name='Profils'),
    re_path(r'^(?P<collaborater_id>[0-9]+)/$', views.Profils, name='Profils'),
    # re_path(r'^GraphCollab(?P<user_id>[0-9]+)/$', views.CompetencesGraphCollab, name='GraphCollab'),
    re_path(r'^DeleteCollab/(?P<collaborater_id>[0-9]+)/$', views.DeleteCollab, name='DeleteCollab'),
    re_path(r'^DeleteUser/(?P<user_id>[0-9]+)/$', views.DeleteUser, name='DeleteUser'),
    re_path(r'^Mon_profil/(?P<user_id>[0-9]+)/$', views.CollaboraterProfil, name='Mon_profil'),
    re_path(r'^Modifier_des_certifications/(?P<profil_id>[0-9]+)/$', views.ModifyInfoCollab, name='Modifier_des_certifications'),
    re_path(r'^Modifier_des_compétences/(?P<listcompetence_id>[0-9]+)/$', views.ModifyCompetenceCollab, name='Modifier_des_compétences'),
    re_path(r'^Ajouter_des_compétences/(?P<user_id>[0-9]+)/$', views.AddCompetenceCollab, name='Ajouter_des_compétences'),
    re_path(r'^Ajouter_des_informations_générales/(?P<user_id>[0-9]+)/$', views.AddInfoCollab, name='Ajouter_des_informations_générales'),
]

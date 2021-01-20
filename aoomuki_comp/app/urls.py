from django.urls import path, re_path
from app import views
from django.contrib.auth import views as authview, authenticate
from django.contrib.auth import views as authview, authenticate
app_name = 'app'

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
    path('login/',authview.LoginView.as_view(template_name="login.html")),
    path('logout/',authview.LogoutView.as_view(template_name="logout.html")),
    path('Formulaire_Compétences_Collaborateur/', views.AllFormlist, name='Formulaire_Compétences_Collaborateur'),
    path('Ajouter_un_utilisateur/collaborateur', views.AddUserAndCollaborater, name='Ajouter_un_utilisateur/collaborateur'),
    path('search/', views.search, name='search'),
    path('Liste_des_collaborateurs/', views.ListCollaboraters, name='Liste_des_collaborateurs'),
    path('Liste_des_utilisateurs/', views.ListUsers, name='Liste_des_utilisateurs'),
    path('Liste_des_domaines/', views.ListField, name='Liste_des_domaines'),
    path('Liste_des_compétences/', views.ListCompetence, name='Liste_des_compétences'),
    path('Liste_des_certifications/', views.ListOfCertification, name='Liste_des_certifications'),
    path('Liste_des_sociétés/', views.ListSociety, name='Liste_des_sociétés'),

    path('Ajouter_Domaines_Compétences/', views.AddFieldCompDegreeSociety, name='Ajouter_Domaines_Compétences'),
    re_path(r'^(?P<collaborater_id>[0-9]+)/$', views.Profils, name='Profils'),
    re_path(r'^DeleteCollab/(?P<collaborater_id>[0-9]+)/$', views.DeleteCollab, name='DeleteCollab'),
    re_path(r'^DeleteUser/(?P<user_id>[0-9]+)/$', views.DeleteUser, name='DeleteUser'),

    # path('Fieldlist/', views.Fieldlist, name='Fieldlist'),

]

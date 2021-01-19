from django.template import loader
from django.http import HttpResponse
from .models import * 
from .forms import AddUserForm, AddFieldForm, AddCompetenceForm, AddCertificationForm, AddSocietyForm, AddCollaboraterForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Prefetch
from django.contrib import messages
from django.contrib.messages import success



def index(request):
    users = User.objects.all()
    context = { 'users':users}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


#liste des collaborateurs
def ListCollaboraters(request):
    collaborater = Collaborater.objects.all().order_by('Lastname') #.order_by('Society')
    context = {
        'collaborater': collaborater,
    }
    return render(request, 'app/Collaboraters_List.html', context)

def ListCollaboratersDelete(request):
    collaborater = Collaborater.objects.all().order_by('Lastname') #.order_by('Society')
    context = {
        'collaborater': collaborater,
    }
    return render(request, 'app/deleteCollaborater.html', context)

def DeleteCollab(request, collaborater_id):
    collaborater = get_object_or_404(Collaborater, pk=collaborater_id)
    context = {
        'collaborater_id': collaborater.id,
    }
    collaborater.delete()
    return render(request, 'app/index.html', context)

def ListUsersDelete(request):
    users = User.objects.all().order_by('Lastname')
    context = {
        'users': users,
    }
    return render(request, 'app/deleteUser.html', context)


def DeleteUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user_id': user.id,
    }
    user.delete()
    return render(request, 'app/index.html', context)


# listes déroulantes issue de la bdd pour le formulaire
def AllFormlist(request): 
    field=Field.objects.all()
    level=ListLevel.objects.all()
    interest=ListInterest.objects.all()
    resultsUser=User.objects.all()
    resultsWorkStation=ListWorkStation.objects.all()
    resultsComp=Competence.objects.all()
    resultsField=Field.objects.all()
    resultsLevel=ListLevel.objects.all()
    resultsCertification=ListCertification.objects.all()
    resultsCollaborater=Collaborater.objects.all()
    resultsInterest=ListInterest.objects.all()
    resultsSociety=Society.objects.all()
    resultsStatut=Statut.objects.all()
    return render(request, "app/form.html",{"showStatut":resultsStatut, "showSociety":resultsSociety, "showComp":resultsComp, "showCertification":resultsCertification, "showCollab":resultsCollaborater, "showWorkStation":resultsWorkStation, "showField":resultsField, "showLevel":resultsLevel, "showInterest":resultsInterest, "showUser":resultsUser, "fields":field, "showLevel":level, "showInterest":interest})




def Profils(request, collaborater_id):
    field=Field.objects.all()
    collaborater = get_object_or_404(Collaborater.objects.prefetch_related(Prefetch('competences', queryset=Competence.objects.only('name', 'field').all()), Prefetch('certification', queryset=ListCertification.objects.only('name').all())), pk=collaborater_id)

    # competence = get_object_or_404(Competence.objects.prefetch_related(Prefetch('interest', queryset=ListInterest.objects.only('value').all())))

    # collaborater = get_object_or_404(Collaborater, pk=collaborater_id)
    # competences = [competence.name for competence in collaborater.competences.all()]
    # competences_name = " ".join(competences)

    # collaborater = Collaborater.objects.all().values('Lastname','Firstname', 'Society', 'competences__name', 'id') 
    context = {
        'collaborater':collaborater,
        'field':field,

        # 'competence':competence,
        # 'collaborater_lastname': collaborater.Lastname,
        # 'collaborater_firstname': collaborater.Firstname,
        # 'collaborater_society': collaborater.Society,
        # 'competences_name': competences_name,
        # 'interests_value': interests.value,

    }
    return render(request, 'app/profil.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'store/search.html', context)

def AddUserAndCollaborater(request):
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = AddUserForm(request.POST)
        if form1.is_valid():
            Lastname = form1.cleaned_data['Lastname']
            Firstname = form1.cleaned_data['Firstname']
            statut = form1.cleaned_data['statut']
            login = form1.cleaned_data['login']
            password = form1.cleaned_data['password']
            user = User.objects.filter(Lastname=Lastname)
            if not user.exists():
                form1.save()
                messages.success(request, "L'utilisateur a été ajouté")
                form1 = AddUserForm()
                form2 = AddCollaboraterForm()
        return render(request, 'app/formAddUser.html', {"form1":form1, "form2":form2})
#*************************************************FAIRE LE 2EME FORMULAIRE DANS CETTE FONCTION************************************************************************
    if request.method == 'POST' and 'btnform2' in request.POST:
        form2 = AddCollaboraterForm(request.POST)
        if form2.is_valid():
            Lastname = form2.cleaned_data['Lastname']
            Firstname = form2.cleaned_data['Firstname']
            statut = form2.cleaned_data['statut']
            Extern = form2.cleaned_data['Extern']
            society = form2.cleaned_data['society']
            collaborater = Collaborater.objects.filter(Lastname=Lastname)
            if not collaborater.exists():
                form2.save()
                messages.success(request, "Le collaborateur a été ajouté")
                form1 = AddUserForm()
                form2 = AddCollaboraterForm()
            return render(request, 'app/formAddUser.html', {"form1":form1, "form2":form2})            
    else:
        form1 = AddUserForm()
        form2 = AddCollaboraterForm()
    return render(request, 'app/formAddUser.html', {'form1': form1, "form2":form2})

# def AddUserAndCollaborater(request):
#     if request.method == 'POST':
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             Lastname = form.cleaned_data['Lastname']
#             Firstname = form.cleaned_data['Firstname']
#             statut = form.cleaned_data['statut']
#             login = form.cleaned_data['login']
#             password = form.cleaned_data['password']
#             user = User.objects.filter(Lastname=Lastname)
#             if not user.exists():
#                 form.save()
#                 messages.success(request, "L'uilisateur a été ajouté")
#                 form = AddUserForm()
#         return render(request, 'app/formAddUser.html', {"form":form})
#     else:
#         # generation de la form initialement vide
#         form = AddUserForm()
#     # retour de la form, soit vide, soit remplie mais avec une erreur, avec un template
#     return render(request, 'app/formAddUser.html', {'form': form})

def ListFieldCollab(request):
    field=Field.objects.all()
    competence=Competence.objects.all()
    context = {
        'field': field,
        'competence': competence,
    }
    return render(request, 'app/ListAddFieldCompetence.html', context)

def AddField(request):
    field=Field.objects.all()
    competence=Competence.objects.all()
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = AddFieldForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            field = Field.objects.filter(name=name)
            if not field.exists():
                form1.save()
                messages.success(request, "Le domaine a été ajouté")
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return render(request, 'app/ListAddFieldCompetence.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

    elif request.method == 'POST' and 'btnform2' in request.POST:
        form2 = AddCompetenceForm(request.POST)
        if form2.is_valid():
            name = form2.cleaned_data['name']
            competence = Competence.objects.filter(name=name)
            if not competence.exists():
                form2.save()
                messages.success(request, "La compétence a été ajoutée")
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return render(request, 'app/ListAddFieldCompetence.html',{'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

    elif request.method == 'POST' and 'btnform3' in request.POST:
        form3 = AddCertificationForm(request.POST)
        if form3.is_valid():
            name = form3.cleaned_data['name']
            certification = ListCertification.objects.filter(name=name)
            if not certification.exists():
                form3.save()
                messages.success(request, "La certification a été ajoutée")
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return render(request, 'app/ListAddFieldCompetence.html',{'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

    elif request.method == 'POST' and 'btnform4' in request.POST:
        form4 = AddSocietyForm(request.POST)
        if form4.is_valid():
            name = form4.cleaned_data['name']
            society = Society.objects.filter(name=name)
            if not society.exists():
                form4.save()
                messages.success(request, "La société a été ajoutée")
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return render(request, 'app/ListAddFieldCompetence.html',{'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

    else:
        form1 = AddFieldForm()
        form2 = AddCompetenceForm()
        form3 = AddCertificationForm()
        form4 = AddSocietyForm()
    return render(request, 'app/ListAddFieldCompetence.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

def search(request):
    query = request.GET.get('query')
    if not query:
        collaborater = Collaborater.objects.all()
    else:
        collaborater = Collaborater.objects.filter(Lastname__icontains=query)
    if not collaborater.exists():
        collaborater = Collaborater.objects.filter(Society__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'collaborater': collaborater,
        # 'name': name,
    }
    return render(request, 'app/search.html', context)


# def user_login(request):
#     """Authenticate a user."""
#     # Etape 1 :
#     login = request.POST["login"]
#     password = request.POST["password"]

#     # Etape 2 :
#     user = authenticate(request, login=login, password=password)

#     # Etape 3 :
#     if user is not None:
#         login(request, user)
#         messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
#     else:
#         messages.add_message(
#             request, messages.ERROR, "Les champs renseignés sont invalides."
#         )

#     return redirect("index.html")


from django.template import loader
from django.http import HttpResponse
from .models import *
from .forms import AddUserForm, AddFieldForm, AddCompetenceForm, AddCertificationForm, AddSocietyForm, AddCollaboraterForm, AddCompCollabForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Prefetch
from django.contrib import messages
from django.contrib.messages import success
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

@login_required
def index(request):
    # users = User.objects.all()
    # context = { 'users':users}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


#liste des collaborateurs
@login_required
def ListCollaboraters(request):
    collaborater = Collaborater.objects.all().order_by('Lastname') #.order_by('Society')
    context = {
        'collaborater': collaborater,
    }
    return render(request, 'app/Collaboraters_List.html', context)

@login_required
def DeleteCollab(request, collaborater_id):
    collaborater = get_object_or_404(Collaborater, pk=collaborater_id)
    context = {
        'collaborater_id': collaborater.id,
    }
    collaborater.delete()
    return render(request, 'app/Collaboraters_List.html', context)

@login_required
def ListUsers(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'app/User_List.html', context)

@login_required
def DeleteUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user_id': user.id,
    }
    user.delete()
    return render(request, 'app/User_List.html', context)


# listes déroulantes issue de la bdd pour le formulaire
@login_required
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



def AddCompetenceCollab(request, user_id):
    
    field = Field.objects.all()
    user = get_object_or_404(User,pk=user_id)
    collaborater = Collaborater.objects.all()
    competence = Competence.objects.all()
    form1 = AddCompCollabForm(initial={'User': request.user.id})
    context = {
        'field': field,
        'user': user,
        'collaborater': collaborater,
        'competence': competence,
        'form1': form1
    }
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = AddCompCollabForm(request.POST,initial={'User': request.user.id})
        if form1.is_valid():
            interest = form1.cleaned_data['ListInterest']
            level = form1.cleaned_data['ListLevel']
            competence = form1.cleaned_data['Competence']
            user = form1.cleaned_data['User']
            form1.save()
            messages.success(request, "Les compétences ont été ajoutées")
            form1 = AddCompCollabForm(initial={'User': request.user.id})
            # form2 = AddCompetenceForm()
        return render(request, 'app/formAddCompetenceCollab.html', context)

    else:
        form1 = AddCompCollabForm()
    return render(request, 'app/formAddCompetenceCollab.html', context)
<<<<<<< HEAD
=======




>>>>>>> 1e58397e39872f95c4a93d2cb358b804220699eb










































@login_required
def Profils(request, collaborater_id):
    field=Field.objects.all()
    collaborater = get_object_or_404(Collaborater.objects.prefetch_related(Prefetch('certification', queryset=ListCertification.objects.only('name').all())), pk=collaborater_id)
    listcompetence = ListofCompetence.objects.all()
    competence=Competence.objects.all()
    level=ListLevel.objects.all()
    interest=ListInterest.objects.all()
    context = {
        'collaborater':collaborater,
        'field':field,
        'listcompetence':listcompetence,
        'competence':competence,
        'level':level,
        'interest':interest
    }
    return render(request, 'app/profil.html', context)

@login_required
def CollaboraterProfil(request, user_id):
    field=Field.objects.all()
    user=get_object_or_404(User,pk=user_id)
    collaborater =Collaborater.objects.all()
    listcompetence = ListofCompetence.objects.all()
    competence=Competence.objects.all()
    level=ListLevel.objects.all()
    interest=ListInterest.objects.all()
    context = {
        'user':user,
        'collaborater':collaborater,
        'field':field,
        'listcompetence':listcompetence,
        'competence':competence,
        'level':level,
        'interest':interest
    }
    return render(request, 'app/profilCollaborater.html', context)

@login_required
def AddCollaborater(request):
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
                form2 = AddCollaboraterForm()
            return render(request, 'app/formAddUser.html', {"form2":form2})            
    else:
        form2 = AddCollaboraterForm()
    return render(request, 'app/formAddUser.html', {'form2': form2})

@login_required
def register(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'utilisateur a été ajouté")
            return redirect(request, 'registration/register.html', {"form":form})
    else:
        form = AddUserForm(request.POST)
    return render(request, 'registration/register.html', {"form":form})

@login_required
def ListField(request):
    field=Field.objects.all()
    context = {
        'field': field,
    }
    return render(request, 'app/Field_List.html', context)

# def AddField(request):
#     field=Field.objects.all()
#     competence=Competence.objects.all()
#     context = {
#         'field': field,
#         'competence': competence,
#     }
#     if request.method == 'POST' and 'btnform1' in request.POST:
#         form1 = AddFieldForm(request.POST)
#         if form1.is_valid():
#             name = form1.cleaned_data['name']
#             field = Field.objects.filter(name=name)
#             if not field.exists():
#                 form1.save()
#                 messages.success(request, "Le domaine a été ajouté")                
#             return render(request, 'app/ListAddFieldCompetence.html', {'form1': form1})

#     else:
#         form1 = AddFieldForm()
#     return render(request, 'app/ListAddFieldCompetence.html', {'form1': form1})
@login_required
def ListCompetence(request):
    competence=Competence.objects.all()
    field=Field.objects.all()
    context = {
        'competence': competence,
        'field': field,

    }
    return render(request, 'app/Competence_List.html', context)

@login_required
def ListOfCertification(request):
    certification=ListCertification.objects.all()
    context = {
        'certification': certification,
    }
    return render(request, 'app/Certification_List.html', context)

@login_required
def ListSociety(request):
    society=Society.objects.all()
    context = {
        'society': society,
    }
    return render(request, 'app/Society_List.html', context)

@login_required
def AddFieldCompDegreeSociety(request):
    field=Field.objects.all()
    competence=Competence.objects.all()
    context = {
        'field': field,
        'competence': competence,
    }
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

@login_required
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



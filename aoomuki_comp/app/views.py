from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import AddUserForm, AddFieldForm, AddCompetenceForm, AddCertificationForm, AddSocietyForm, AddCompCollabForm , ProfilForm ,ModifyProfilForm, ModifyCompetenceForm, AddCollaboraterForm #CollaboraterForm #AddCollaboraterForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Prefetch
from django.contrib import messages
from django.contrib.messages import success, error
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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


#*********************************************************************************************************liste des collaborateurs
@login_required
def ListCollaboraters(request):
    collaborater = Collaborater.objects.all().order_by('collaborater') #.order_by('Society')
    context = {
        'collaborater': collaborater,
    }
    return render(request, 'app/Collaboraters_List.html', context)

@login_required
def DeleteCollab(request, collaborater_id):
    collab = get_object_or_404(Collaborater, pk=collaborater_id)
    context = {
        'collab': collab,
    }
    collab.delete()
    messages.success(request, "Le collaborateur a été supprimé")
    return render(request, 'app/Collaboraters_List.html', context)
#*********************************************************************************************************supprimer un collab
@login_required
def ListUsers(request):
    profil = UserProfil.objects.all()
    users = User.objects.all()
    context = {
        'profil': profil,
        'users': users,
    }
    return render(request, 'app/User_List.html', context)

@login_required
def DeleteUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user_id': user.id,
    }
    return render(request, 'app/User_List.html', context)

# def ProfilsAdmin(request, user_id):
#     user=get_object_or_404(User, pk=user_id)
#     field=Field.objects.all()
#     profil = UserProfil.objects.all()
#     listcompetence = ListofCompetence.objects.all()
#     competence=Competence.objects.all()
#     level=ListLevel.objects.all()
#     interest=ListInterest.objects.all()
#     context = {
#         'profil':profil,
#         'field':field,
#         'listcompetence':listcompetence,
#         'competence':competence,
#         'level':level,
#         'interest':interest,
#         'user':user,
#     }
#     return render(request, 'app/ProfilsAdmin.html', context)

@login_required
def AddCompetenceCollab(request, user_id):
    profil = UserProfil.objects.all()
    collaborater = Collaborater.objects.all()
    certification = ListCertification.objects.all()
    user = get_object_or_404(User,pk=user_id)
    listcompetence = ListofCompetence.objects.all()
    competence = Competence.objects.all()
    form1 = AddCompCollabForm()
    context = {
        'user': user,
        'profil': profil,
        'listcompetence': listcompetence,
        'form1': form1,
        'collaborater': collaborater,
    }
    if request.method == 'POST' and 'btnform1' in request.POST: #and request.is_ajax
        if request.user.is_authenticated:
            form1 = AddCompCollabForm(request.POST)
            if form1.is_valid():
                interest = form1.cleaned_data['ListInterest']
                level = form1.cleaned_data['ListLevel']
                competence = form1.cleaned_data['Competence']
                listcomp = ListofCompetence.objects.filter(User_id=user_id, Competence=competence)
                if not listcomp.exists():
                    formComp = form1.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                    formComp.User = User.objects.get(pk=request.user.id) 
                    formComp.save() # sauvergarde tout cette fois ci
                    messages.success(request, "La compétences a été ajoutée")
                    form1 = AddCompCollabForm()
                    return render(request, 'app/formAddCompetenceCollab.html', context)
                else:
                    messages.error(request, "Vous avez déjà ajouté cette compétence")
    else:
        form1 = AddCompCollabForm()
        form2 = ProfilForm()
        context = {
        'user': user,
        'profil': profil,
        'listcompetence': listcompetence,
        'form1': form1,
        'collaborater': collaborater,
        }
    return render(request, 'app/formAddCompetenceCollab.html', context)

@login_required
def ModifyCompetenceCollab(request, listcompetence_id ):
    listcompetence = get_object_or_404(ListofCompetence,pk=listcompetence_id)
    form4 = ModifyCompetenceForm(instance=listcompetence)
    context = {
        'listcompetence': listcompetence,
        'form4': form4
    }
    if request.method == 'POST' and 'btnform2' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form4 = ModifyCompetenceForm(request.POST, instance=listcompetence)
            if form4.is_valid():
                interest = form4.cleaned_data['ListInterest']
                level = form4.cleaned_data['ListLevel']
                competence = form4.cleaned_data['Competence']
                formComp3 = form4.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                formComp3.save() # sauvergarde tout cette fois ci
                # data = {
                # 'message':'form is saved'
                # }
                # return JsonResponse(data)
                messages.success(request, "La compétence a été modifiée")
                form4 = ModifyCompetenceForm()
                return render(request, 'app/profilCollaborater.html', context)
    else:
        form3 = ModifyCompetenceForm(instance=listcompetence)
        context = {
        'listcompetence': listcompetence,
        'form4': form4
        }
    return render(request, 'app/FormModifyCompetenceCollab.html', {'form3': form3})

def AddCollabForm(request):
    collaborater = Collaborater.objects.all()
    form6 = AddCollaboraterForm()
    context = {
        'collaborater': collaborater,
        'form6': form6,
    }
    if request.method == 'POST' and 'btnform1' in request.POST:
        form6 = AddCollaboraterForm(request.POST)
        if form6.is_valid():
            collaborater = form6.cleaned_data['collaborater']
            user = form6.cleaned_data['user']
            collaborater = Collaborater.objects.filter(user=user)
            if not collaborater.exists():
                form6.save()
                messages.success(request, "Le collaborater a été ajouté")
                form6 = AddCollaboraterForm()
                return render(request, 'app/FormAddCollab.html', context)
            else:
                messages.error(request, "Ce collaborateur existe déjà")
    else:
        form6 = AddCollaboraterForm()
        context = {
            'collaborater': collaborater,
            'form6': form6,
        }
    return render(request, 'app/FormAddCollab.html', context)


@login_required
def AddInfoCollab(request, user_id):
    profil = UserProfil.objects.all()
    user = get_object_or_404(User,pk=user_id)
    form2 = ProfilForm()
    # form5 = CollaboraterForm()
    context = {
        'user': user,
        'profil': profil,
        'form2': form2,
        # 'form5': form5
    }
    if request.method == 'POST' and 'btnform2' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form2 = ProfilForm(request.POST)
            if form2.is_valid():
                society = form2.cleaned_data['society']
                Extern = form2.cleaned_data['Extern']
                workstation = form2.cleaned_data['workstation']
                profil = UserProfil.objects.filter(user=user_id)
                if not profil.exists():
                    formComp1 = form2.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                    formComp1.user = User.objects.get(pk=request.user.id) 
                    formComp1.save() # sauvergarde tout cette fois ci
                    form2.save_m2m()#sauvergarde le champs manytomany
                    messages.success(request, "Le profil a été ajouté.")
                    return render(request, 'app/formAddInformationCollab.html', context)
                else:
                    messages.error(request, "Vous étes déja enregistré en tant que collaborateur ")
            # 
            # 
            #             # if form5.is_valid():
            #     collaborater = form5.cleaned_data['collaborater']
            #     collaborater = Collaborater.objects.filter(user=user_id)
            #     if not collaborater.exists():
            #         formComp2 = form5.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
            #         formComp2.user = User.objects.get(pk=request.user.id)
            #         formComp2.save() # sauvergarde tout cette fois ci

            # if form2.is_valid() and form5.is_valid():
            #     collaborater = Collaborater.objects.filter(user=user_id)
            #     profil = UserProfil.objects.filter(user=user_id)
            #     if not profil.exists() and not collaborater.exists():
            #         messages.success(request, "Le profil a été ajouté.")
            #         return render(request, 'app/formAddInformationCollab.html', context)
            #     else:
            #         messages.error(request, "Vous étes déja enregistré en tant que collaborateur ")

    else:
        form2 = ProfilForm()
        # form5 = CollaboraterForm()
        context = {
        'user': user,
        'profil': profil,
        'form2': form2,
        # 'form5': form5
        }
    return render(request, 'app/formAddInformationCollab.html', context)

@login_required
def ModifyInfoCollab(request, profil_id, ):
    profil = get_object_or_404(UserProfil,pk=profil_id)
    form3 = ModifyProfilForm(instance=profil)
    context = {
        'profil': profil,
        'form3': form3
    }
    if request.method == 'POST' and 'btnform2' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form3 = ModifyProfilForm(request.POST, instance=profil)
            if form3.is_valid():
                society = form3.cleaned_data['society']
                Extern = form3.cleaned_data['Extern']
                workstation = form3.cleaned_data['workstation']
                formComp2 = form3.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                formComp2.save() # sauvergarde tout cette fois ci
                form3.save_m2m()#sauvergarde le champs manytomany
                # data = {
                # 'message':'form is saved'
                # }
                # return JsonResponse(data)
                messages.success(request, "Le profil a été modifié")
                form3 = ModifyProfilForm()
                return render(request, 'app/FormModifyInfoCollab.html', context)
    else:
        form3 = ModifyProfilForm(instance=profil)
        context = {
        'profil': profil,
        'form3': form3
        }
    return render(request, 'app/FormModifyInfoCollab.html', context)


@login_required
def Profils(request, collaborater_id):
    user=User.objects.all()
    collaborater = get_object_or_404(Collaborater, pk=collaborater_id)
    field=Field.objects.all()
    profil = UserProfil.objects.all()
    listcompetence = ListofCompetence.objects.all()
    competence=Competence.objects.all()
    level=ListLevel.objects.all()
    interest=ListInterest.objects.all()
    context = {
        'profil':profil,
        'field':field,
        'listcompetence':listcompetence,
        'competence':competence,
        'level':level,
        'interest':interest,
        'collaborater':collaborater,
        'user':user,
    }
    return render(request, 'app/profil.html', context)

@login_required
def CollaboraterProfil(request, user_id):
    collaborater = Collaborater.objects.all()
    profil = UserProfil.objects.all()
    field=Field.objects.all()
    user=get_object_or_404(User,pk=user_id)
    listcompetence = ListofCompetence.objects.all()
    competence=Competence.objects.all()
    level=ListLevel.objects.all()
    interest=ListInterest.objects.all()
    context = {
        'user':user,
        'collaborater':collaborater,
        'profil':profil,
        'field':field,
        'listcompetence':listcompetence,
        'competence':competence,
        'level':level,
        'interest':interest
    }
    return render(request, 'app/profilCollaborater.html', context)


@login_required
def register(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'utilisateur a été ajouté")
            return render(request, 'registration/register.html', {"form":form})
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



def CompetencesGraph(request):
    return render(request, 'app/GraphCompetences.html')
    # return render(request, 'app/GraphCompetences.html')
    
    

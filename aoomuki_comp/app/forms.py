from django.forms import ModelForm, TextInput, EmailInput, FileInput, PasswordInput, Select, CheckboxInput,RadioSelect
from django.forms.utils import ErrorList
from django import forms
from .models import Field, Competence, ListCertification, Society, Collaborater, ListofCompetence
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory

# class ParagraphErrorList(ErrorList):
#     def __str__(self):
#         return self.as_divs()
#     def as_divs(self):
#         if not self: return ''
#         return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username"]
        # widgets = {
        #     'Lastname': TextInput(attrs={'class': 'form-control'}),
        #     'Firstname': TextInput(attrs={'class': 'form-control'}),
        #     'statut':Select(attrs={'class': 'form-control'}),
        #     'login': TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput()
        # }

class AddCollaboraterForm(ModelForm):
    class Meta:
        model = Collaborater
        fields = ["Lastname", "Firstname", "society", "statut", "Extern", "workstation", "user"]
        widgets = {
            'Lastname': TextInput(attrs={'class': 'form-control'}),
            'Firstname': TextInput(attrs={'class': 'form-control'}),
            'statut':Select(attrs={'class': 'form-control'}),
            'society': Select(attrs={'class': 'form-control'}),
            'workstation':Select(attrs={'class': 'form-control'}),
            'Extern':CheckboxInput(attrs={'class': 'form-control'}),
            'user':Select(attrs={'class': 'form-control'}),

        }

<<<<<<< HEAD
class AddCompCollabForm(ModelForm):
    
    class Meta:
        model = ListofCompetence
        fields = [ "ListInterest", "ListLevel", "User"]
        widgets = {
            'User': forms.HiddenInput(),
            # 'Collaborater': Select(attrs={'class': 'select','style':'width: 150px'}),
            'ListInterest': RadioSelect(attrs={'class': 'select','style':'width: 150px'}),
            'ListLevel':RadioSelect(attrs={'class': 'select','style':'width: 150px'}),
=======
class AddCompCollabForm(forms.ModelForm):
    class Meta:
        model = ListofCompetence
        fields = [ "User","Competence", "ListInterest", "ListLevel" ]
        widgets = {
            'User': Select(attrs={'class': 'select','style':'width: 150px'}),
            'Competence': Select(attrs={'class': 'select','style':'width: 150px'}),
            'ListInterest': Select(attrs={'class': 'select','style':'width: 150px'}),
            'ListLevel':Select(attrs={'class': 'select','style':'width: 150px'}),
>>>>>>> aa29f99d0ccf6266448d962349975b6083f5cf71
        }
        # form.fields['user'].initial = 'Romuald'
        # def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user','')
        # super(AddCompCollabForm, self).__init__(*args, **kwargs)
        # self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))


class AddFieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

class AddCompetenceForm(ModelForm):
    class Meta:
        model = Competence
        fields = ["name", "field"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'field':Select(attrs={'class': 'form-control'}),
        }

class AddCertificationForm(ModelForm):
    class Meta:
        model = ListCertification
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

class AddSocietyForm(ModelForm):
    class Meta:
        model = Society
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


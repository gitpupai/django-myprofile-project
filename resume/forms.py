from django import forms
from django.forms import ModelForm
from .models import City, State, Profile, Certification, Award, Course, Experience, Skill, FLUENCY_CHOICES as fluency_choices

from django.db import models
# from django.forms import ClearableFileInput

cities = City.objects.all()
states = State.objects.all()



city_choices=[]
for city in cities:
    city_choices.append((city.id,city))


state_choices=[]
for state in states:
    state_choices.append((state.id,state))

# Profile Form
class ProfileForm(ModelForm):

    class Meta:
        model= Profile
        fields = ['first_name','last_name','email','dp','city_id','state_id','objective','facebook','linkedin']



# Certificate Forms

class CreateCertificateForm(forms.Form):

    name = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)


class AddCertificateForm(forms.Form):
    certificatesList=[(certificate.id,certificate) for certificate in Certification.objects.all()]
    def __init__(self,*args,**kwargs):
        super(AddCertificateForm,self).__init__(*args,**kwargs)
        self.fields["name"] = forms.ChoiceField(choices=[(certificate.id,certificate) for certificate in Certification.objects.all()])
    url = forms.URLField()
    year = forms.DateField()


## Award Forms

class CreateAwardForm(forms.Form):

    name = forms.CharField(max_length=50)
    source = forms.CharField(max_length=50)


class AddAwardForm(forms.Form):

    def __init__(self,*args,**kwargs):
        super(AddAwardForm,self).__init__(*args,**kwargs)
        self.fields["name"] = forms.ChoiceField(choices=[(award.id,award) for award in Award.objects.all()])
    recognition = forms.CharField(max_length=30)
    year = forms.DateField()



## Course Forms

class CreateCourseForm(forms.Form):
    name = forms.CharField(max_length=50)


class AddCourseForm(forms.Form):

    def __init__(self,*args,**kwargs):
        super(AddCourseForm,self).__init__(*args,**kwargs)
        self.fields["name"] = forms.ChoiceField(choices=[(course.id,course) for course in Course.objects.all()])
    year=forms.DateField()
    marks=forms.FloatField()
    total_marks=forms.FloatField()
    college=forms.CharField(max_length=50)
    specialization=forms.CharField(max_length=50)


## Experience Forms

class CreateExperienceForm(forms.Form):
    role = forms.CharField(max_length=50)


class AddExperienceForm(forms.Form):

    def __init__(self,*args,**kwargs):
        super(AddExperienceForm,self).__init__(*args,**kwargs)
        self.fields["role"] = forms.ChoiceField(choices=[(experience.id,experience) for experience in Experience.objects.all()])
    start_year=forms.DateField()
    end_year=forms.DateField(required=False)
    company=forms.CharField(max_length=50)


class CreateSkillForm(forms.Form):
    name = forms.CharField(max_length=30)


class AddSkillForm(forms.Form):
    FLUENCY_CHOICES=(
        ('BR','Beginner'),
        ('IN','Intermediate'),
        ('EX','Expert')
    )

    def __init__(self,*args,**kwargs):
        super(AddSkillForm,self).__init__(*args,**kwargs)
        self.fields["name"] = forms.ChoiceField(choices=[(skill.id,skill) for skill in Skill.objects.all()])
    fluency=forms.ChoiceField(choices=[fluency for fluency in fluency_choices])

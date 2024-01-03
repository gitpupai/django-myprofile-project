from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
FLUENCY_CHOICES=(
    ('BR','Beginner'),
    ('IN','Intermediate'),
    ('EX','Expert')
)


class Award(models.Model):
    name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)

    def __str__(self):
        return self.name + " from " +self.source


class Skill(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



class State(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name=models.CharField(max_length=100)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Viewer(models.Model):
    viewer=models.TextField(default=None)
    # liked=models.BooleanField(default=False)
    def __str__(self):
        return self.viewer


class Profile(models.Model):

    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50, unique=True)
    dp=models.ImageField(upload_to='resume/images/dps/')
    objective=models.TextField(max_length=500)
    city_id=models.ForeignKey(City,on_delete=models.CASCADE, default=None)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE, default=None)
    facebook=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,  default=None)

    def __str__(self):
        return self.first_name + " " +self.last_name


class Certification(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)

    def __str__(self):
        return self.name + " from " +self.company


class certificateProfile(models.Model):
    certificate_id=models.ForeignKey(Certification,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    url=models.URLField(blank=True)
    year=models.DateField()


class Course(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class courseProfile(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    year=models.DateField()
    marks=models.FloatField(max_length=100)
    total_marks=models.FloatField(max_length=100)
    college=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)

    class Meta:
        ordering = ['-year']


class awardProfile(models.Model):
    award_id=models.ForeignKey(Award,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    recognition=models.CharField(max_length=30)
    year=models.DateField()


class Experience(models.Model):
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.role


class experienceProfile(models.Model):
    experience_id=models.ForeignKey(Experience,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    start_year=models.DateField()
    end_year=models.DateField(blank=True)
    company=models.CharField(max_length=50,  default=None)

    class Meta:
        ordering = ['-end_year']

    def __str__(self):
        return self.experience_id.role + " in " + self.company


class skillProfile(models.Model):
    skill_id=models.ForeignKey(Skill,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    fluency = models.CharField(choices=FLUENCY_CHOICES,max_length=2)



class viewerProfile(models.Model):
    viewer_id = models.ForeignKey(Viewer,on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    liked=models.BooleanField(default=False)

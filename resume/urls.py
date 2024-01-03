from django.urls import path
from . import views

app_name='resume'

urlpatterns = [
 # path('',views.show_resume,name='show_resume'),
 path('<int:pk>/',views.show_resume.as_view(),name='show_resume'),

 # profile apis
 path('api/profiles',views.ProfileList.as_view()),
 path('api/<int:pk>/profileprofilelist',views.ProfileProfileList.as_view()),
 path('api/<int:pk>/profileprofiledelete',views.ProfileProfileDelete.as_view()),

 # certificates apis
 path('api/certificates',views.CertificateList.as_view()),
 path('api/<int:cpk>/certificateprofiledelete',views.CertificateProfileDelete.as_view()),
 path('api/<int:pk>/certificateprofilelist',views.CertificateProfileList.as_view()),
 path('api/certificateprofilecreate',views.CertificateProfileCreate.as_view()),

 # courses apis
 path('api/courses',views.CourseList.as_view()),
 path('api/<int:cpk>/courseprofiledelete',views.CourseProfileDelete.as_view()),
 path('api/<int:pk>/courseprofilelist',views.CourseProfileList.as_view()),
 path('api/courseprofilecreate',views.CourseProfileCreate.as_view()),

 # awards apis
 path('api/awards',views.AwardList.as_view()),
 path('api/<int:apk>/awardprofiledelete',views.AwardProfileDelete.as_view()),
 path('api/<int:pk>/awardprofilelist',views.AwardProfileList.as_view()),
 path('api/awardprofilecreate',views.AwardProfileCreate.as_view()),

 # experience apis
 path('api/experiences',views.ExperienceList.as_view()),
 path('api/<int:epk>/experienceprofiledelete',views.ExperienceProfileDelete.as_view()),
 path('api/<int:pk>/experienceprofilelist',views.ExperienceProfileList.as_view()),
 path('api/experienceprofilecreate',views.ExperienceProfileCreate.as_view()),

 ## SKill apis
 path('api/skills',views.SkillList.as_view()),
 path('api/<int:spk>/skillprofiledelete',views.SkillProfileDelete.as_view()),
 path('api/<int:pk>/skillprofilelist',views.SkillProfileList.as_view()),
 path('api/skillprofilecreate',views.SkillProfileCreate.as_view()),

 path('makeprofile',views.MakeProfile.as_view(), name='makeprofile'),

## Edit on certificates
 path('createcertificate',views.CreateCertificate.as_view(), name='createcertificate'),
 path('addcertificate',views.AddCertificate.as_view(), name='addcertificate'),
 path('deletecertificate',views.DeleteCertificate.as_view(), name='deletecertificate'),

## Edit on awards
 path('createaward',views.CreateAward.as_view(), name='createaward'),
 path('addaward',views.AddAward.as_view(), name='addaward'),
 path('deleteaward',views.DeleteAward.as_view(), name='deleteaward'),

 ##edit on Course
 path('createcourse',views.CreateCourse.as_view(), name='createcourse'),
 path('addcourse',views.AddCourse.as_view(), name='addcourse'),
 path('deletecourse',views.DeleteCourse.as_view(), name='deletecourse'),

 ##Edit on Experience
 path('createexperience',views.CreateExperience.as_view(), name='createexperience'),
 path('addexperience',views.AddExperience.as_view(), name='addexperience'),
 path('deleteexperience',views.DeleteExperience.as_view(), name='deleteexperience'),

 ##Edit on Skill
 path('createskill',views.CreateSkill.as_view(), name='createskill'),
 path('addskill',views.AddSkill.as_view(), name='addskill'),
 path('deleteskill',views.DeleteSkill.as_view(), name='deleteskill'),

 ## Delete Profile
 path('deleteprofile',views.DeleteProfile.as_view(), name='deleteprofile'),


 ## Search Profile
 path('searchprofile',views.SearchProfile.as_view(),name='searchprofile'),
]

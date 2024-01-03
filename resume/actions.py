from .models import Viewer,Skill,Profile,Certification,Course,Award,Experience,certificateProfile, City, State, courseProfile, awardProfile, experienceProfile, skillProfile, viewerProfile
import socket
import requests
import json
from rest_framework.parsers import JSONParser
from .forms import ProfileForm
from requests.auth import HTTPBasicAuth
from datetime import date
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

host = '127.0.0.1'
port = '8000'

def isExist(ip):
    print("isExist")
    ipFromDB=Viewer.objects.filter(viewer=ip)

    if len(ipFromDB)>0:
        viewer=Viewer.objects.get(viewer=ip)
        return True

    return False


def getIP():
    print("getIP")
    IPAddr = socket.gethostbyname(socket.gethostname())
    return IPAddr


def viewerExists(ip):
    if not isExist(ip):
        return False
    return True


def viewer_profile_exists(ip,pk):
    try:
        viewer = Viewer.objects.get(viewer=ip)
        profile = Profile.objects.get(id=pk)
        viewer_profile = viewerProfile.objects.get(viewer_id=viewer,profile_id=profile)
        return True
    except ObjectDoesNotExist:
        return False


def save_viewer_profile(ip,pk):
    viewer = Viewer.objects.get(viewer=ip)
    profile = Profile.objects.get(id=pk)
    viewer_profile = viewerProfile(viewer_id=viewer,profile_id=profile)
    viewer_profile.save()


def get_viewer_count(pk):
    profile = Profile.objects.get(id=pk)
    count = viewerProfile.objects.filter(profile_id=profile).count()
    return count


def get_viewer_profile(ip,pk):
    viewer = Viewer.objects.get(viewer=ip)
    profile = Profile.objects.get(id=pk)
    viewer_profile = viewerProfile.objects.get(viewer_id=viewer,profile_id=profile)
    return viewer_profile


# def delete_all_viewer(profile):
#     viewer_profile = viewerProfile.objects.filter(profile_id=profile)
#     print(viewer_profile)
#     # for vp in viewer_profile:
#     #     vp.delete()


def increaseLike(pk):
    ip=getIP()
    viewer = Viewer.objects.get(viewer=ip)
    profile = Profile.objects.get(id=pk)
    vp=viewerProfile.objects.get(viewer_id=viewer,profile_id=profile)
    if vp.liked:
        vp.liked=False
        vp.save()
        return False

    vp.liked=True
    vp.save()
    return True


def get_likes(pk):
    like=viewerProfile.objects.filter(profile_id=Profile.objects.get(id=pk),liked="True").count()
    return like


def getCertificate(profile):
    certificate_profile=certificateProfile.objects.filter(profile_id=profile.id)
    cp=[]
    for i in certificate_profile:
        cp.append((i,i.certificate_id))

    return cp

def get_profile(pk):
    url=f"http://{host}:{port}/profile/api/{pk}/profileprofilelist"
    response=requests.get(url)
    profile=json.loads(response.content)

    return profile


def get_courseProfile(pk):
    url=f"http://{host}:{port}/profile/api/{pk}/courseprofilelist"
    response=requests.get(url)
    course_list=json.loads(response.content)

    return course_list


def get_certificateProfile(pk):
    url=f"http://{host}:{port}/profile/api/{pk}/certificateprofilelist"
    response=requests.get(url)
    certificate_list=json.loads(response.content)

    return certificate_list

def get_awardProfile(pk):

    url=f"http://{host}:{port}/profile/api/{pk}/awardprofilelist"
    response=requests.get(url)
    award_list=json.loads(response.content)

    return award_list

def get_experienceProfile(pk):
    url=f"http://{host}:{port}/profile/api/{pk}/experienceprofilelist"
    response=requests.get(url)
    experience_list=json.loads(response.content)

    return experience_list


def get_skillProfile(pk):
    url=f"http://{host}:{port}/profile/api/{pk}/skillprofilelist"
    response=requests.get(url)
    skill_list=json.loads(response.content)

    return skill_list


def get_skillname(skill_list):
    skill_ids=[]
    print(skill_list)
    for skill in skill_list:
        skill_ids.append(skill['skill_id'])

    skill_name=[]
    for skill_id in skill_ids:
        skill_name.append(Skill.objects.filter(id=skill_id))

    return skill_name


def divide(A,time):

    if len(A)%time==0:
        window=len(A)//time
    else:
        window=len(A)//time + 1

    separated=[]
    x=0
    y=0
    while x<window:
        n=0
        divide=[]
        while n<time and y<len(A):
            divide.append(A[y])
            y+=1
            n+=1
        separated.append(divide)
        x+=1

    return separated

def get_cities():
    cities=City.objects.all()
    return cities

def get_city_id(name):
    city=City.objects.get(name=name)
    return city.id

def get_states():
    states=State.objects.all()
    return states

def get_state_id(name):
    state=State.objects.get(name=name)
    return state.id

def get_profile_details(form,request):
    profile_details={}
    # profile_details['first_name']= request.POST.get('fname')
    # profile_details['last_name']= request.POST.get('lname')
    # profile_details['email']= request.POST.get('email')
    # profile_details['city_id']= get_city_id(request.POST.get('city'))
    # profile_details['state_id']= get_state_id(request.POST.get('state'))
    # profile_details['objective']= request.POST.get('objective')
    # profile_details['facebook']= request.POST.get('facebook')
    # profile_details['linkedin']= request.POST.get('linkedin')
    # profile_details['dp']= request.POST.get('dpname')

    profile_details['first_name']= form.cleaned_data["first_name"]
    profile_details['last_name']= form.cleaned_data["last_name"]
    profile_details['email']= form.cleaned_data["email"]
    # profile_details['dp']= form.cleaned_data["dp"]
    # print(TemporaryUploadedFile.temporary_file_path(form.cleaned_data["dp"]))
    # profile_details['dp']=TemporaryUploadedFile.temporary_file_path(form.cleaned_data["dp"])
    profile_details['city_id']= form.cleaned_data["city_id"]
    profile_details['state_id']= form.cleaned_data["state_id"]
    profile_details['objective']= form.cleaned_data["objective"]
    profile_details['facebook']= form.cleaned_data["facebook"]
    profile_details['linkedin']= form.cleaned_data["linkedin"]
    profile_details['user']= request.user

    return profile_details


def create_profile(profile_details):

    print(profile_details)

    url = f"http://{host}:{port}/profile/api/profiles"
    data = profile_details

    response=requests.post(url=url,data=data)
    print(response)
    return


def create_new_profile(form,user):

    if form.is_valid():
        newprofile = form.save(commit=False)
        newprofile.user = user
        newprofile.save()
        return 1

    else:
        return 2


def edit_profile(form,user):

    if form.is_valid():
        form.save()
        return 3
    else:
        return 2


def isExist_profile(user):
    existCount=Profile.objects.filter(user=user).count()

    if existCount>=1:
        return False
    else:
        return True


def validate(course_id,profile_id):
    print(course_id,profile_id)
    record = courseProfile.objects.filter(course_id=course_id,profile_id=profile_id.id)
    if len(record)>=1:
        print("already available")
        return False
    else:
        print("not available")
        return True


    # url=f"http://127.0.0.1:8000/profile/api/{pk}/awardprofilelist"
    # response=requests.get(url)
    # award_list=json.loads(response.content)
    #
    # return award_list

def get_token(profile_id):
    profile = Profile.objects.get(id=profile_id)
    user = User.objects.get(id=profile.user_id)
    token = Token.objects.get(user=user)
    return token.key

## Run APIs ###########################################################################
def create(details,str):
    url = f"http://{host}:{port}/profile/api/{str}"
    response=requests.post(url=url,data=details)
    return response


def add(details,token,str):
    url = f"http://{host}:{port}/profile/api/{str}profilecreate"
    headers = {'Authorization':'token '+token}

    response=requests.post(url=url,data=details, headers = headers)
    return response


def delete(id,token,str):
    url = f"http://{host}:{port}/profile/api/{id}/{str}profiledelete"
    headers = {'Authorization':'token '+token}
    response=requests.delete(url=url, headers = headers)
    return response

########################################################################################

'''
Cerificate functiom
'''
def get_certificate_details(form,request):

    certificate_details={}
    name = request.POST.get('name')
    company = request.POST.get('company')

    certificate_details['name']=name
    certificate_details['company']=company

    return certificate_details


def create_certificate(certificate_details):
    return create(certificate_details,'certificates')


def add_certificate_details(form,request):

    certificateprofile_details={}
    certificate_id = request.POST.get('name')
    cert_url = request.POST.get('url')
    year = request.POST.get('year')
    profile_id = Profile.objects.get(user=request.user)

    certificateprofile_details['certificate_id'] = certificate_id
    certificateprofile_details['url'] = cert_url
    certificateprofile_details['year'] = year
    certificateprofile_details['profile_id'] = profile_id.id

    print(certificateprofile_details)

    return certificateprofile_details


def add_certificate(certificateprofile_details):
    token = get_token(certificateprofile_details['profile_id'])
    return add(certificateprofile_details,token,'certificate')


def deletecertificate(certificate_profile):
    id = certificate_profile.id
    token = get_token(certificate_profile.profile_id.id)
    return delete(id,token,'certificate')


def certificate_exists(certificate_details):
    try:
        isExist= Certification.objects.get(name=certificate_details["name"],company=certificate_details["company"])
        return True
    except ObjectDoesNotExist:
        return False


'''
Award functiom
'''

def get_award_details(form, request):

    award_details={}
    name = request.POST.get('name')
    source = request.POST.get('source')

    award_details['name']=name
    award_details['source']=source

    return award_details


def create_award(award_details):
    return create(award_details,'awards')


def add_award_details(form,request):

    awardprofile_details={}
    award_id = request.POST.get('name')
    award_recog = request.POST.get('recognition')
    year = request.POST.get('year')
    profile_id = Profile.objects.get(user=request.user)

    awardprofile_details['award_id'] = award_id
    awardprofile_details['recognition'] = award_recog
    awardprofile_details['year'] = year
    awardprofile_details['profile_id'] = profile_id.id

    print(awardprofile_details)

    return awardprofile_details


def add_award(awardprofile_details):
    token = get_token(awardprofile_details['profile_id'])
    return add(awardprofile_details,token,'award')


def deleteaward(award_profile):
    id = award_profile.id
    token = get_token(award_profile.profile_id.id)
    return delete(id,token,'award')

def award_exists(award_details):
    try:
        isExist= Award.objects.get(name=award_details["name"],source=award_details["source"])
        return True
    except ObjectDoesNotExist:
        return False

'''
Course functiom
'''
def get_course_details(form, request):

    course_details={}
    name = request.POST.get('name')
    course_details['name']=name

    return course_details


def create_course(course_details):
    return create(course_details,'courses')


def add_course_details(request):

    courseprofile_details={}
    course_id = request.POST.get('name')
    year = request.POST.get('year')
    profile_id = Profile.objects.get(user=request.user)
    marks=request.POST.get('marks')
    total_marks=request.POST.get('total_marks')
    college=request.POST.get('college')
    specialization=request.POST.get('specialization')

    if validate(course_id,profile_id):

        courseprofile_details['course_id'] = course_id
        courseprofile_details['year'] = year
        courseprofile_details['profile_id'] = profile_id.id
        courseprofile_details['marks'] = float(marks)
        courseprofile_details['total_marks'] = float(total_marks)
        courseprofile_details['college'] = college
        courseprofile_details['specialization'] = specialization

        print(courseprofile_details)

    return courseprofile_details


def add_course(courseprofile_details):
    token = get_token(courseprofile_details['profile_id'])
    return add(courseprofile_details,token,'course')


def deletecourse(course_profile):
    id = course_profile.id
    token = get_token(course_profile.profile_id.id)
    return delete(id,token,'course')


def course_exists(course_details):
    try:
        isExist= Course.objects.get(name=course_details["name"])
        return True
    except ObjectDoesNotExist:
        return False


'''
Experience functiom
'''

def get_experience_details(request):

    experience_details={}
    role = request.POST.get('role')
    experience_details['role']=role

    return experience_details


def create_experience(experience_details):
    return create(experience_details,'experiences')


def add_experience_details(request):

    experienceprofile_details={}
    experience_id = request.POST.get('role')
    start_year = request.POST.get('start_year')
    end_year = request.POST.get('end_year')
    profile_id = Profile.objects.get(user=request.user)
    company = request.POST.get('company')


    experienceprofile_details['experience_id'] = experience_id
    experienceprofile_details['start_year'] = start_year
    experienceprofile_details['end_year'] = end_year
    experienceprofile_details['profile_id'] = profile_id.id
    experienceprofile_details['company'] = company

    print(experienceprofile_details)

    return experienceprofile_details


def add_experience(experienceprofile_details):
    if experienceprofile_details['end_year']=='':
        experienceprofile_details['end_year']=date.today()
    token = get_token(experienceprofile_details['profile_id'])
    return add(experienceprofile_details,token,'experience')


def deleteexperience(experience_profile):
    id = experience_profile.id
    token = get_token(experience_profile.profile_id.id)
    return delete(id,token,'experience')


def experience_exists(experience_details):
    try:
        isExist= Experience.objects.get(role=experience_details["role"])
        return True
    except ObjectDoesNotExist:
        return False

'''
Skill
'''

def get_skill_details(request):
    skill_details={}
    name = request.POST.get('name')
    skill_details['name']=name

    return skill_details


def create_skill(skill_details):
    return create(skill_details,'skills')


def add_skill_details(request):

    skillprofile_details={}
    skill_id = request.POST.get('name')
    fluency = request.POST.get('fluency')
    profile_id = Profile.objects.get(user=request.user)


    skillprofile_details['skill_id'] = skill_id
    skillprofile_details['profile_id'] = profile_id.id
    skillprofile_details['fluency'] = fluency

    print(skillprofile_details)

    return skillprofile_details


def add_skill(skillprofile_details):
    token = get_token(skillprofile_details['profile_id'])
    return add(skillprofile_details,token,'skill')


def deleteskill(skill_profile):
    id = skill_profile.id
    token = get_token(skill_profile.profile_id.id)
    return delete(id,token,'skill')

def skill_exists(skill_details):
    try:
        isExist= Skill.objects.get(name=skill_details["name"])
        return True
    except ObjectDoesNotExist:
        return False


def is_skillProfile_exists(skillprofile_details):
    try:
        isExist = skillProfile.objects.get(skill_id=skillprofile_details["skill_id"],profile_id=skillprofile_details["profile_id"])
        return True
    except ObjectDoesNotExist:
        return False

############################ Delete All Modules ##################################

def delete_all_certificates(profile):

    modules=certificateProfile.objects.filter(profile_id=profile.id)

    for module in modules:
        state = deletecertificate(module)
        if not state.ok:
            return False
    return True


def delete_all_courses(profile):

    modules=courseProfile.objects.filter(profile_id=profile.id)

    for module in modules:
        state = deletecourse(module)
        if not state.ok:
            return False
    return True



def delete_all_awards(profile):

    modules=awardProfile.objects.filter(profile_id=profile.id)

    for module in modules:
        state = deleteaward(module)
        if not state.ok:
            return False
    return True

def delete_all_experiences(profile):

    modules=experienceProfile.objects.filter(profile_id=profile.id)

    for module in modules:
        state = deleteexperience(module)
        if not state.ok:
            return False
    return True

def delete_all_skills(profile):

    modules=skillProfile.objects.filter(profile_id=profile.id)

    for module in modules:
        state = deleteskill(module)
        if not state.ok:
            return False
    return True


def deleteprofile(profile):
    id=profile.id
    token = get_token(id)

    url = f"http://{host}:{port}/profile/api/{id}/profileprofiledelete"
    headers = {'Authorization':'token '+token}
    response=requests.delete(url=url, headers = headers)
    return response


def get_profiles(request):
    query = request.GET['searchname']
    search_profiles = Profile.objects.filter(first_name__icontains=query) | Profile.objects.filter(last_name__icontains=query)
    return search_profiles


def get_my_profile(request):
    profiles = Profile.objects.filter(user_id=request.user)
    if len(profiles)>0:
        profile = profiles[0]

    return profile

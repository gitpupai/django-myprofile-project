from django.shortcuts import render, redirect
import requests
from .actions import viewerExists,getIP,increaseLike,getCertificate,get_profile, get_courseProfile, divide, get_certificateProfile, get_experienceProfile, get_awardProfile, get_cities, get_states, create_new_profile, get_city_id, get_state_id, get_profile_details, isExist_profile, get_certificate_details, create_certificate, add_certificate_details, add_certificate, deletecertificate, get_award_details, create_award, add_award_details, add_award, deleteaward, get_course_details, create_course, add_course_details, add_course, deletecourse, get_experience_details, create_experience, add_experience_details, add_experience, deleteexperience, get_skill_details, create_skill, add_skill_details, add_skill, deleteskill, get_skillProfile, get_skillname, delete_all_certificates, delete_all_courses, delete_all_awards, delete_all_experiences, delete_all_skills, deleteprofile, get_profiles, edit_profile, certificate_exists, award_exists, course_exists, experience_exists, skill_exists, is_skillProfile_exists, viewer_profile_exists, save_viewer_profile, get_viewer_count, get_viewer_profile, get_likes
from . models import Award,awardProfile,Certification,Viewer,Profile,certificateProfile, Course, courseProfile, Experience, experienceProfile, City, Skill, skillProfile, viewerProfile
from . serializers import CertificationSerializer,CertificateProfileSerializer,CourseSerializer,CourseProfileSerializer,AwardProfileSerializer,AwardSerializer,ExperienceSerializer, ExperienceProfileSerializer, ProfileSerializer, SkillSerializer, SkillProfileSerializer
from rest_framework import generics, mixins, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.views import View
from .forms import ProfileForm, CreateCertificateForm, AddCertificateForm, CreateAwardForm, AddAwardForm, CreateCourseForm, AddCourseForm, CreateExperienceForm, AddExperienceForm, CreateSkillForm, AddSkillForm
from datetime import datetime
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from json import JSONDecodeError
import json


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileProfileList(generics.ListAPIView):

    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        profile_profile= Profile.objects.filter(id=profile.id)
        return profile_profile


class ProfileProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        profile_profile= Profile.objects.filter(id=profile.id)
        return profile_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')



class CertificateList(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

    # get the User from request and save the post with the user user
    # def perform_create(self,serializer):
    #     serializer.save(poster=self.request.user)

class CertificateProfileList(generics.ListAPIView):

    serializer_class = CertificateProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        certificate_profile= certificateProfile.objects.filter(profile_id=profile)
        return certificate_profile


class CertificateProfileCreate(generics.ListCreateAPIView):

    queryset = certificateProfile.objects.all()
    serializer_class = CertificateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertificateProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):
    serializer_class = CertificateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        certificate_profile= certificateProfile.objects.filter(pk=self.kwargs['cpk'])
        return certificate_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    #     serializer.save(poster=self.request.user)

class CourseProfileList(generics.ListAPIView):
    # queryset = courseProfile.objects.all()
    serializer_class = CourseProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        course_profile= courseProfile.objects.filter(profile_id=profile)
        return course_profile


class CourseProfileCreate(generics.ListCreateAPIView):

    queryset = courseProfile.objects.all()
    serializer_class = CourseProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):
    serializer_class = CourseProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_profile= courseProfile.objects.filter(pk=self.kwargs['cpk'])
        return course_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')


class AwardList(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class AwardProfileList(generics.ListAPIView):

    serializer_class = AwardProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        award_profile= awardProfile.objects.filter(profile_id=profile)
        return award_profile

class AwardProfileCreate(generics.ListCreateAPIView):

    queryset = awardProfile.objects.all()
    serializer_class = AwardProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AwardProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):
    serializer_class = AwardProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        award_profile= awardProfile.objects.filter(pk=self.kwargs['apk'])
        return award_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')


class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceProfileList(generics.ListAPIView):
    serializer_class = ExperienceProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        experience_profile= experienceProfile.objects.filter(profile_id=profile)
        print(experience_profile)
        return experience_profile


class ExperienceProfileCreate(generics.ListCreateAPIView):

    queryset = experienceProfile.objects.all()
    serializer_class = ExperienceProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.POST.get('end_year') > self.request.POST.get('start_year'):
            serializer.save()
        else:
            raise ValidationError('Future Date error')


class ExperienceProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):
    serializer_class = ExperienceProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        # experience= Experience.objects.get(pk=self.kwargs['ek'])
        experience_profile= experienceProfile.objects.filter(pk=self.kwargs['epk'])
        print(experience_profile)
        # profile= Profile.objects.get(pk=self.kwargs['pk'])
        # experience_profile= experienceProfile.objects.filter(experience_id=experience,profile_id=profile)
        return experience_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')


class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillProfileList(generics.ListAPIView):

    serializer_class = SkillProfileSerializer

    def get_queryset(self):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        skill_profile= skillProfile.objects.filter(profile_id=profile)
        return skill_profile


class SkillProfileCreate(generics.ListCreateAPIView):

    queryset = skillProfile.objects.all()
    serializer_class = SkillProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class SkillProfileDelete(generics.ListAPIView, mixins.DestroyModelMixin):

    serializer_class = SkillProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        skill_profile= skillProfile.objects.filter(pk=self.kwargs['spk'])
        return skill_profile

    def delete(self,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Not Available')



class show_resume(View):

    def get(self,request,pk):

        try:
            ip=getIP()
            if not viewerExists(ip):
                viewer=Viewer(viewer=ip)
                viewer.save()


            pk=self.kwargs['pk']
            if not viewer_profile_exists(ip,pk):
                save_viewer_profile(ip,pk)

            count = get_viewer_count(pk)
            # print(f'total viewer is {count}')
            like = get_likes(pk)
            # print(f'total likes {like}')
            ## view Profile
            profile=get_profile(pk)
            ## view Courses
            course=divide(get_courseProfile(pk),2)
            ## View Certificates
            certificate = get_certificateProfile(pk)
            ## View Awards
            award = get_awardProfile(pk)
            ## View Experiences
            experience = divide(get_experienceProfile(pk),2)
            ## View Skills
            skill = get_skillProfile(pk)
            ## View Viewers
            vp = get_viewer_profile(ip,pk)

            return render(request,'resume/resume.html',{'counts':count,'likes':like,'skills':skill,'profiles':profile,'certificates':certificate,'courses':course,'awards':award,'experiences':experience,'vps':vp})

        except (JSONDecodeError, ObjectDoesNotExist) as error:
            return render(request,'account/homepage.html')


    def post(self,request,pk):
        if request.method=="POST":
            if not increaseLike(pk):
                pass

        return self.get(request,pk)


class MakeProfile(View):

    def get(self,request):
        if request.user.id:
            profiles = Profile.objects.filter(user_id=request.user)
            if len(profiles)>0:
                profile = Profile.objects.get(id=profiles[0].id)
                form=ProfileForm(instance = profile)
            else:
                form=ProfileForm()
            return render(request,'resume/makeprofile.html',{'forms':form})
        else:
            return render(request,'resume/makeprofile.html')


    def post(self,request):
        user=request.user

        success=0
        profiles = Profile.objects.filter(user_id=user)
        if len(profiles)>0:
            profile = Profile.objects.get(id=profiles[0].id)
            form=ProfileForm(request.POST, request.FILES, instance = profile)
        else:
            form=ProfileForm(request.POST, request.FILES)

        if isExist_profile(user):
            success= create_new_profile(form,user)
        else:
            success= edit_profile(form,user)

        return render(request,'resume/makeprofile.html',{'forms':form,'success':success})


class CreateCertificate(View):

    def get(self,request):

        form = CreateCertificateForm()

        return render(request,'resume/createmodule.html',{'form':form,'module':'Certificate'})


    def post(self,request):

        success =0
        form = CreateCertificateForm(request.POST)

        certificate_details = get_certificate_details(form,request)

        if not certificate_exists(certificate_details):
            status = create_certificate(certificate_details)

            if status.ok:
                success=1
            else:
                success = 2

        else:
            success = 3

        return render(request,'resume/createmodule.html',{'form':form,'success':success,'module':'Certificate'})



class AddCertificate(View):

    def get(self,request):
        form = AddCertificateForm()
        profile = Profile.objects.filter(user_id=request.user.id)
        getmessage = True
        if len(profile)>0:
            return render(request,'resume/addmodule.html',{'form':form,'module':'Certificate','getmessage':getmessage})
        else:
            getmessage=False
            return render(request,'resume/addmodule.html',{'getmessage':getmessage,'module':'Certificate'})


    def post(self,request):

        getmessage = True
        success=0

        form = AddCertificateForm(request.POST)
        certificateprofile_details = add_certificate_details(form,request)

        status = add_certificate(certificateprofile_details)

        if status.ok:
            success=1
        else:
            success = 2
        return render(request,'resume/addmodule.html',{'form':form,'success':success,'module':'Certificate','getmessage':getmessage})



class DeleteCertificate(View):

    def get(self,request):
        if request.user.id:
            try:
                profile=Profile.objects.get(user=request.user)
                cp=certificateProfile.objects.filter(profile_id=profile.id)
                return render(request,'resume/deletecertificate.html',{'cps':cp})

            except ObjectDoesNotExist:
                return render(request,'account/homepage.html')
        else:
            return render(request,'resume/deletecertificate.html')


    def post(self,request):

        try:
            success=0
            cp_id = request.POST.get('cp_id')
            certificate_profile = certificateProfile.objects.get(id=cp_id)

            status = deletecertificate(certificate_profile)

            if status.ok:
                success=1
            else:
                success = 2

            profile=Profile.objects.get(user=request.user)
            cp=certificateProfile.objects.filter(profile_id=profile.id)

            return render(request,'resume/deletecertificate.html',{'cps':cp,'success':success})

        except ObjectDoesNotExist:
            return render(request,'resume/deletecertificate.html')



class CreateAward(View):

    def get(self,request):

        form = CreateAwardForm()

        return render(request,'resume/createmodule.html',{'form':form,'module':'Award'})


    def post(self,request):

        success =0
        form = CreateAwardForm(request.POST)

        award_details = get_award_details(form,request)

        if not award_exists(award_details):
            status = create_award(award_details)

            if status.ok:
                success=1
            else:
                success = 2

        else:
            success = 3

        return render(request,'resume/createmodule.html',{'form':form,'success':success,'module':'Award'})



class AddAward(View):

    def get(self,request):

        form = AddAwardForm()
        profile = Profile.objects.filter(user_id=request.user.id)
        getmessage = True
        if len(profile)>0:
            return render(request,'resume/addmodule.html',{'form':form,'module':'Award','getmessage':getmessage})
        else:
            getmessage=False
            return render(request,'resume/addmodule.html',{'getmessage':getmessage})

    def post(self,request):

        getmessage = True
        success=0

        form = AddAwardForm(request.POST)
        awardprofile_details = add_award_details(form,request)

        status = add_award(awardprofile_details)

        if status.ok:
            success=1
        else:
            success = 2
        return render(request,'resume/addmodule.html',{'form':form,'success':success,'module':'Award','getmessage':getmessage})



class DeleteAward(View):

    def get(self,request):
        if request.user.id:

            try:
                profile=Profile.objects.get(user=request.user)
                ap=awardProfile.objects.filter(profile_id=profile.id)
                return render(request,'resume/deleteaward.html',{'aps':ap})

            except ObjectDoesNotExist:
                return render(request,'account/homepage.html')

        else:
            return render(request,'resume/deleteaward.html')


    def post(self,request):

        try:
            success=0
            ap_id = request.POST.get('ap_id')
            award_profile = awardProfile.objects.get(id=ap_id)

            status = deleteaward(award_profile)

            if status.ok:
                success=1
            else:
                success = 2

            profile=Profile.objects.get(user=request.user)
            ap=experienceProfile.objects.filter(profile_id=profile.id)

            return render(request,'resume/deleteaward.html',{'aps':ap,'success':success})

        except ObjectDoesNotExist:
            return render(request,'resume/deleteaward.html')



class CreateCourse(View):

    def get(self,request):

        form = CreateCourseForm()

        return render(request,'resume/createmodule.html',{'form':form,'module':'Course'})


    def post(self,request):

        success =0
        form = CreateCourseForm(request.POST)

        course_details = get_course_details(form,request)

        if not course_exists(course_details):
            status = create_course(course_details)

            if status.ok:
                success=1
            else:
                success = 2

        else:
            success = 3

        return render(request,'resume/createmodule.html',{'form':form,'success':success,'module':'Course'})


class AddCourse(View):

    def get(self,request):

        form = AddCourseForm()
        profile = Profile.objects.filter(user_id=request.user.id)
        getmessage = True
        if len(profile)>0:
            return render(request,'resume/addmodule.html',{'form':form,'module':'Course','getmessage':getmessage})
        else:
            getmessage=False
            return render(request,'resume/addmodule.html',{'getmessage':getmessage})

    def post(self,request):

        getmessage = True
        success=0

        form = AddCourseForm(request.POST)
        courseprofile_details = add_course_details(request)
        if not bool(courseprofile_details):
            success=3
        else:
            status = add_course(courseprofile_details)

            if status.ok:
                success=1
            else:
                success = 2
        return render(request,'resume/addmodule.html',{'form':form,'success':success,'module':'Course','getmessage':getmessage})



class DeleteCourse(View):

    def get(self,request):
        if request.user.id:
            try:
                profile=Profile.objects.get(user=request.user)
                cp=courseProfile.objects.filter(profile_id=profile.id)
                return render(request,'resume/deletecourse.html',{'cps':cp})
            except ObjectDoesNotExist:
                return render(request,'account/homepage.html')

        else:
            return render(request,'resume/deletecourse.html')


    def post(self,request):

        try:
            success=0
            cp_id = request.POST.get('cp_id')
            course_profile = courseProfile.objects.get(id=cp_id)

            status = deletecourse(course_profile)

            if status.ok:
                success=1
            else:
                success = 2

            profile=Profile.objects.get(user=request.user)
            cp=courseProfile.objects.filter(profile_id=profile.id)

            return render(request,'resume/deletecourse.html',{'cps':cp,'success':success})

        except ObjectDoesNotExist:
            return render(request,'resume/deletecourse.html')


class CreateExperience(View):

    def get(self,request):

        form = CreateExperienceForm()

        return render(request,'resume/createmodule.html',{'form':form,'module':'Experience'})


    def post(self,request):

        success =0
        form = CreateExperienceForm(request.POST)

        experience_details = get_experience_details(request)

        if not experience_exists(experience_details):
            status = create_experience(experience_details)

            if status.ok:
                success=1
            else:
                success = 2

        else:
            success = 3

        return render(request,'resume/createmodule.html',{'form':form,'success':success,'module':'Experience'})



class AddExperience(View):

    def get(self,request):

        form = AddExperienceForm()
        profile = Profile.objects.filter(user_id=request.user.id)
        getmessage = True
        if len(profile)>0:
            return render(request,'resume/addmodule.html',{'form':form,'module':'Experience','getmessage':getmessage})
        else:
            getmessage=False
            return render(request,'resume/addmodule.html',{'getmessage':getmessage})

    def post(self,request):

        getmessage = True
        success=0

        form = AddExperienceForm(request.POST)
        experienceprofile_details = add_experience_details(request)

        print(experienceprofile_details)
        status = add_experience(experienceprofile_details)

        if status.ok:
            success=1
        else:
            status=json.loads(status.content)[0]
            success = 2
        return render(request,'resume/addmodule.html',{'form':form,'success':success,'module':'Experience','getmessage':getmessage,'status':status})



class DeleteExperience(View):

    def get(self,request):
        if request.user.id:
            try:
                profile=Profile.objects.get(user=request.user)
                ep=experienceProfile.objects.filter(profile_id=profile.id)
                return render(request,'resume/deleteexperience.html',{'eps':ep})
            except ObjectDoesNotExist:
                return render(request,'account/homepage.html')

        else:
            return render(request,'resume/deleteexperience.html')

    def post(self,request):

        try:
            success=0
            ep_id = request.POST.get('ep_id')
            experience_profile = experienceProfile.objects.get(id=ep_id)

            status = deleteexperience(experience_profile)

            if status.ok:
                success=1
            else:
                success = 2

            profile=Profile.objects.get(user=request.user)
            ep=experienceProfile.objects.filter(profile_id=profile.id)

            return render(request,'resume/deleteexperience.html',{'eps':ep,'success':success})

        except ObjectDoesNotExist:
            return render(request,'resume/deleteexperience.html')


class CreateSkill(View):

    def get(self,request):

        form = CreateSkillForm()

        return render(request,'resume/createmodule.html',{'form':form,'module':'Skill'})


    def post(self,request):

        success =0
        form = CreateSkillForm(request.POST)

        skill_details = get_skill_details(request)

        if not skill_exists(skill_details):
            status = create_skill(skill_details)

            if status.ok:
                success=1
            else:
                success = 2

        else:
            success = 3

        return render(request,'resume/createmodule.html',{'form':form,'success':success,'module':'Skill'})


class AddSkill(View):

    def get(self,request):

        form = AddSkillForm()
        profile = Profile.objects.filter(user_id=request.user.id)
        getmessage = True
        if len(profile)>0:
            return render(request,'resume/addmodule.html',{'form':form,'module':'Skill','getmessage':getmessage})
        else:
            getmessage = False
            return render(request,'resume/addmodule.html',{'getmessage':getmessage})

    def post(self,request):

        getmessage = True
        success=0

        form = AddSkillForm(request.POST)
        skillprofile_details = add_skill_details(request)

        if not is_skillProfile_exists(skillprofile_details):
            status = add_skill(skillprofile_details)

            if status.ok:
                success=1
            else:
                success = 2
        else:
            success = 3

        return render(request,'resume/addmodule.html',{'form':form,'success':success,'module':'Skill','getmessage':getmessage})



class DeleteSkill(View):

    def get(self,request):
        if request.user.id:
            try:
                profile=Profile.objects.get(user=request.user)
                sp=skillProfile.objects.filter(profile_id=profile.id)
                return render(request,'resume/deleteskill.html',{'sps':sp})

            except ObjectDoesNotExist:
                return render(request,'account/homepage.html')
        else:
            return render(request,'resume/deleteskill.html')


    def post(self,request):

        try:
            success=0
            sp_id = request.POST.get('sp_id')
            skill_profile = skillProfile.objects.get(id=sp_id)

            status = deleteskill(skill_profile)

            if status.ok:
                success=1
            else:
                success = 2

            profile=Profile.objects.get(user=request.user)
            sp=skillProfile.objects.filter(profile_id=profile.id)

            return render(request,'resume/deleteskill.html',{'sps':sp,'success':success})

        except ObjectDoesNotExist:
            return render(request,'resume/deleteskill.html')



class DeleteProfile(View):

    def post(self,request):

        success=0
        try:
            profile=Profile.objects.get(user=request.user)
        except:
            success=3
            print(success)
            return redirect('account:homepage')

        print(profile.id)

        ## Transaction starts
        state_certificate = delete_all_certificates(profile)
        state_course = delete_all_courses(profile)
        state_award = delete_all_awards(profile)
        state_experience = delete_all_experiences(profile)
        state_skill = delete_all_skills(profile)

        if state_certificate and state_course and state_award and state_experience and state_skill:
            status = deleteprofile(profile)

        ## Transaction ends

        if status.ok:
            success=1
        else:
            success = 2

        print(profile)
        return render(request,'account/homepage.html',{'success':success})



class SearchProfile(View):

    def get(self,request):

        search_profile = get_profiles(request)
        return render(request,'account/searchpage.html',{'search_profiles':search_profile})

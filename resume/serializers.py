from rest_framework import serializers
from .models import Profile,Certification,certificateProfile,Course,courseProfile,Award,awardProfile, City, State, Experience, experienceProfile, Skill, skillProfile
from datetime import datetime


class ProfileSerializer(serializers.ModelSerializer):

    # user= serializers.ReadOnlyField(source='user.id')

    city_name=serializers.SerializerMethodField()
    state_name=serializers.SerializerMethodField()

    class Meta:
        model=Profile
        fields=['id','first_name','last_name','email','dp','objective','city_id','city_name','state_id','state_name','facebook','linkedin','user']


    def get_city_name(self, profile):

        profile=Profile.objects.get(id=profile.id)
        city=City.objects.get(id=profile.city_id.id)

        return city.name


    def get_state_name(self, profile):

        profile=Profile.objects.get(id=profile.id)
        state=State.objects.get(id=profile.state_id.id)

        return state.name



class CertificationSerializer(serializers.ModelSerializer):
    ##to make the poster read only, we dont have to post it explicitly
    # poster = serializers.ReadOnlyField(source='poster.username')
    # profile_id = serializers.ReadOnlyField(source='poster.id')
    # certificates= serializers.SerializerMethodField()
    # profile_id = serializers.ReadOnlyField(source='poster.id')
    profile_count = serializers.SerializerMethodField()

    class Meta:
        model=Certification
        fields=['id','name','company','profile_count']

    def get_profile_count(self, certificate):

        return certificateProfile.objects.filter(certificate_id=certificate.id).count()


class CertificateProfileSerializer(serializers.ModelSerializer):

    certificate_name=serializers.SerializerMethodField()
    company=serializers.SerializerMethodField()

    class Meta:
        model=certificateProfile
        fields=['id','profile_id','certificate_id','certificate_name','company','url','year']

    def get_certificate_name(self, certificate_profile):

        certificate_profile=certificateProfile.objects.get(id=certificate_profile.id)
        certificate=Certification.objects.get(id=certificate_profile.certificate_id.id)

        return certificate.name

    def get_company(self, certificate_profile):

        certificate_profile=certificateProfile.objects.get(id=certificate_profile.id)
        certificate=Certification.objects.get(id=certificate_profile.certificate_id.id)

        return certificate.company


class CourseSerializer(serializers.ModelSerializer):

    profile_count = serializers.SerializerMethodField()

    class Meta:
        model=Course
        fields=['id','name','profile_count']

    def get_profile_count(self, course):

        return courseProfile.objects.filter(course_id=course.id).count()


class CourseProfileSerializer(serializers.ModelSerializer):

    percentage=serializers.SerializerMethodField()
    course_name=serializers.SerializerMethodField()

    class Meta:
        model=courseProfile
        fields=['id','profile_id','course_id','course_name','college','year','specialization','marks','total_marks','percentage']


    def get_percentage(self, course_profile):

        course_profile=courseProfile.objects.get(id=course_profile.id)
        marks=course_profile.marks
        total_marks=course_profile.total_marks

        return round((marks/total_marks)*100,1)

    def get_course_name(self, course_profile):

        course_profile=courseProfile.objects.get(id=course_profile.id)
        course=Course.objects.get(id=course_profile.course_id.id)

        return course.name


class AwardSerializer(serializers.ModelSerializer):

    profile_count = serializers.SerializerMethodField()

    class Meta:
        model=Award
        fields=['id','name','source','profile_count']

    def get_profile_count(self, award):

        return awardProfile.objects.filter(award_id=award.id).count()


class AwardProfileSerializer(serializers.ModelSerializer):

    award_name=serializers.SerializerMethodField()
    source=serializers.SerializerMethodField()

    class Meta:
        model=awardProfile
        fields=['id','profile_id','award_id','award_name','source','recognition','year']

    def get_award_name(self, award_profile):

        award_profile=awardProfile.objects.get(id=award_profile.id)
        award=Award.objects.get(id=award_profile.award_id.id)

        return award.name

    def get_source(self, award_profile):

        award_profile=awardProfile.objects.get(id=award_profile.id)
        award=Award.objects.get(id=award_profile.award_id.id)

        return award.source



class ExperienceSerializer(serializers.ModelSerializer):

    profile_count = serializers.SerializerMethodField()

    class Meta:
        model=Experience
        fields=['id','role','profile_count']

    def get_profile_count(self, experience):

        return experienceProfile.objects.filter(experience_id=experience.id).count()


class ExperienceProfileSerializer(serializers.ModelSerializer):

    years_of_experience=serializers.SerializerMethodField()
    experience_role=serializers.SerializerMethodField()

    class Meta:
        model=experienceProfile
        fields=['id','profile_id','experience_id','experience_role','company','start_year','end_year','years_of_experience']


    def get_years_of_experience(self, experience_profile):

        experience_profile=experienceProfile.objects.get(id=experience_profile.id)
        print(experience_profile.end_year,experience_profile.start_year)
        yoe=experience_profile.end_year - experience_profile.start_year
        yoe_seconds=yoe.total_seconds()
        years_of_experience=(((yoe_seconds/3600)/24)/365)

        return round(years_of_experience,2)

    def get_experience_role(self, experience_profile):

        experience_profile=experienceProfile.objects.get(id=experience_profile.id)
        experience=Experience.objects.get(id=experience_profile.experience_id.id)

        return experience.role


class SkillSerializer(serializers.ModelSerializer):

    profile_count = serializers.SerializerMethodField()

    class Meta:
        model=Skill
        fields=['id','name','profile_count']

    def get_profile_count(self, skill):

        return skillProfile.objects.filter(skill_id=skill.id).count()


class SkillProfileSerializer(serializers.ModelSerializer):

    skill_name=serializers.SerializerMethodField()

    class Meta:
        model=skillProfile
        fields=['id','profile_id','skill_id','skill_name','fluency']

    def get_skill_name(self, skill_profile):

        skill_profile=skillProfile.objects.get(id=skill_profile.id)
        skill=Skill.objects.get(id=skill_profile.skill_id.id)

        return skill.name

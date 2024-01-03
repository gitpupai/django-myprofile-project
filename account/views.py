from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from resume.models import Profile

# Create your views here.
class SignUp(View):

    success= 0

    def get(self,request):
        print('getsignup')
        return render(request, 'account/signup.html',{'form':UserCreationForm})

    @csrf_exempt
    def post(self,request):
        success=0
        try:
            # data=JSONParser().parse(request)
            if request.POST['password1']==request.POST['password2']:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                token = Token.objects.create(user=user)
                success=1
                return render(request, 'account/signup.html',{'success':success,'token':str(token),'form':UserCreationForm})
            else:
                # tell the user password mismatch
                success=2
                return render(request, 'account/signup.html',{'success':success,'form':UserCreationForm})
        except IntegrityError:
            success = 3
            return render(request,'account/signup.html',{'success':success,'form':UserCreationForm})

class SignIn(View):

    def get(self,request):
        return render(request, 'account/signin.html',{'form':AuthenticationForm})

    def post(self,request):
        success=0
        user= authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'account/signin.html',{'form':AuthenticationForm,'success':success})
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            login(request,user)
            success=1
            return redirect('account:homepage')





class HomePageView(View):

    def get(self,request):
        print("get homepage")
        profile=None
        if request.user.id:
            profiles = Profile.objects.filter(user_id=request.user)
            if len(profiles)>0:
                profile=profiles[0]
        return render(request, 'account/homepage.html',{'profiles':profile})

    def post(self,request):
        if "logoutButton" in request.POST:
            logout(request)
            return render(request, 'account/homepage.html')
        else:
            return render(request, 'account/homepage.html')



class About(View):

    def get(self,request):
        return render(request, 'account/about.html')


class Contact(View):

    def get(self,request):
        return render(request, 'account/contact.html')

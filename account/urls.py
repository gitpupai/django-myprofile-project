from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('home',views.HomePageView.as_view(),name='homepage'),
    path('signin',views.SignIn.as_view(),name='signin'),
    path('signup',views.SignUp.as_view(),name='signup'),
    path('about',views.About.as_view(),name='about'),
    path('contact',views.Contact.as_view(),name='contact'),
]

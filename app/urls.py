from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('about/',views.about,name='about'),
  path('do/',views.do,name='do'),
  path('portfolio/',views.portfolio,name='portfolio'),
  path('contact/',views.contact,name='contact'),
]

from django.urls import path
from . import views
app_name="basicE"
urlpatterns = [
    path('templates/', views.basicE_template, name='basicE_template'),
    path('templates/basicE_form_show', views.basicE_form_show, name='basicE_form_show'),
    path('templates/basicE_form', views.basicE_form, name='basicE_form'),
    path('templates/basicE_form_show2', views.basicE_form_show2, name='basicE_form_show2'),
    path('templates/basicE_form2', views.basicE_form2, name='basicE_form2'),
    path('templates/basicE_form_show3', views.basicE_form_show3, name='basicE_form_show3'),
    path('templates/basicE_form_show4', views.basicE_form_show4, name='basicE_form_show4'),
    path('templates/basicE_form4', views.basicE_form4, name='basicE_form4'),
]

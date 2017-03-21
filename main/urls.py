#!C:/Users/arif/AppData/Local/Programs/Python/Python35-32/python.exe
from django.conf.urls import url
from main import views
urlpatterns =[
    url(r'^$', views.main_page),
    url(r'^portfolio/$', views.portfolio),
    url(r'^projects/$', views.project),
    url(r'^contacts/$', views.contacts),
    url(r'^send/$', views.sendemail)

]
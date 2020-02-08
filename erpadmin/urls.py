from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_admin, name='addAdmin'),
    path('viewAdmins', views.view_admins, name='viewAdmins'),
]

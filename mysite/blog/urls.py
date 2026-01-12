from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name = 'home'),
    path('/projects', views.ProjectView.as_view(), name = "projects")
]
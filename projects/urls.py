from django.urls import path
from . import views
# For storing the url patterns


urlpatterns = [
    path('', views.projects, name="projects"),  # root domain
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name = "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name = "delete-project"),

]

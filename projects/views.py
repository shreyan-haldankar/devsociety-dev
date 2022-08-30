import profile
from re import search
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from projects.utils import paginateProjects, searchProjects
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
# Create your views here.
# Business logic / Functions will be made here


# Creating a view
def projects(request):
    projects, search_query = searchProjects(request)
    custom_range,projects = paginateProjects(request, projects, 6)

    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile

        review.save()

        projectObj.getVoteCount
        messages.success(request, "Your Review was successfully submitted!")
        return redirect('project', pk=projectObj.id)

        # Update Project vote count

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form':form})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST , request.FILES)
        # print(request.POST) # THe actual data
        # If the request method is post then process the data
        if form.is_valid():  # will check if the form has any errors
            project = form.save(commit=False)  # It will create that object and add it to the database
            # once the form is submitted we want to take the user to the projects page
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect("account")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)

# The update part

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    # It is gonna check the primary key of the project and pre fill the data inside the Model Form with the existing data
    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        # print(request.POST) # THe actual data
        # If the request method is post then process the data
        if form.is_valid():  # will check if the form has any errors
            project = form.save()  # It will create that object and add it to the database
            # once the form is submitted we want to take the user to the projects page
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect("account")

    context = {"form": form, 'project': project}
    return render(request, "projects/project_form.html", context)


# Deleting a Project
@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "delete_template.html", context)


# Django 4's templating engine uses Jinja

# Passing variables to a webpage using {{ var_name }}

# Create a list of dictionaries for outputting more dynamic data


# For executing a query
# queryset = ModelName.objects.all()

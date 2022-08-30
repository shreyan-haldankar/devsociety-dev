import re
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag

from api import serializers

# GET is the request method


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},  # takes us to a specific project
        # When we wanna vote a specific project
        {'POST': '/api/projects/id/vote'},

        # Built in routes for generating tokens for a user
        {'POST': '/api/users/token'},
        # used after a token gets expired to stay logged in
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    # many = True because we are serializing many objects
    serializer = ProjectSerializer(projects, many=True)
    # serializer is used for serializing the Projects model and to access the data we do serializer.data
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    # We are querying a single project
    # many = False because we are serializing just one object
    serializer = ProjectSerializer(project, many=False)
    # serializer is used for serializing the Projects model and to access the data we do serializer.data
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    review.value = data['value']
    review.save()

    project.getVoteCount
    # because we use app property decorator we dont have to trigger it as a function
    # For running the getting vote count method
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)
    return Response('Tag was deleted!')

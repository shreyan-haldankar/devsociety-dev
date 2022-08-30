from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # overriding owner field to serialize its objects
    owner = ProfileSerializer(many = False) # As there is only one owner
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    # We are adding the review attribute here
    class Meta:
        model = Project
        fields = '__all__'

    # We have to start our methods with get
    # Here self will be the Class here i.e ProjectSerializer and obj will be the model i.e Project 
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializers = ReviewSerializer(reviews, many = True) # here we will serialize the reviews query set into JSON object
        return serializers.data
        # This will return reviews as an object
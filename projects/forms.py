from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = "__all__"
        # fields that we want the user to input
        fields = ["title", "featured_image" , "description", "demo_link", "source_link"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        # Now we can customize the fields
        # self.fields['title'].widget.attrs.update({'class':'input'})
        # # input is a css class
        # # we can modify multiple css classes such as placeholder etc

        # self.fields['description'].widget.attrs.update({'class':'input'})
        # We can do it faster using a for loop
        

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
            'value':"Place your vote",
            'body': 'Add your comment with a vote'
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
from django.db import models
from django.utils.timezone import utc
from django.forms import ModelForm
from django.utils import timezone
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)
    
    
class PostForm(ModelForm):
    class Meta:
            model = Post
            fields = ['title', 'body' , 'active']
			
class EditForm(ModelForm):
    class Meta:
            model = Post
            fields = ['title', 'body' , 'active', 'completed']			
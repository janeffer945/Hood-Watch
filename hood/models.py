from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
class Business(models.Model):
    # image = models.ImageField(default='default.jpg', upload_to='hood_pics')
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=250)
    # neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)  
    
        
    def __str__(self):
        return self.name
    
class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    # image = models.ImageField(default='default.jpg', upload_to='hood_pics')
    image = CloudinaryField('image')
    description = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=250)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    health_cell = models.IntegerField(null=True, blank=True)
    police_hotline = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['-updated_on', '-created_on']
        
            
    def __str__(self):
        return self.name
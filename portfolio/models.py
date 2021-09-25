from django.db import models
from PIL import Image
# Create your models here.

class Project(models.Model):
    name = models.CharField( max_length=255)
    url_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    description = models.CharField(max_length=255,blank=True)
    description_long = models.TextField(blank=True)
    gitLink = models.CharField(max_length=255,blank=True)
    liveLink = models.CharField(max_length=255,blank=True)
    mainImage = models.ImageField(default='default.jpg', upload_to='project_images')

    def __str__(self):
        return self.name
    
    #Resize large images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.mainImage.path)
        
        if img.height>300 or img.width>600:
            output_size = (600,300)
            img.thumbnail(output_size)
            img.save(self.mainImage.path)
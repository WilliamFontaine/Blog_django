from django.db import models

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.TextField()
    
    def __str__(self):
        return self.titre
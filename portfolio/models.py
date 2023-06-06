from django.db import models

class Project(models.Model):
    # Field to store the title of the project
    title = models.CharField(max_length=100)
    # Field to store the description of the project
    description = models.CharField(max_length=250)
    # Field to store the image of the project
    image = models.ImageField(upload_to='portfolio/images/')
    # Optional field to store the URL of the project
    url = models.URLField(blank=True)
    
    def __str__(self):
        # Return the title of the project as its string representation
        return self.title
from django.db import models

class Blog(models.Model):
    # Field for the blog title
    title = models.CharField(max_length=200)
    # Field for the blog date
    date = models.DateField()
    # Field for the blog description
    description = models.TextField()

    
    def __str__(self):
        # Returns the title as a string representation of the object
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Model for the pictures
class Picture(models.Model):
    image = models.ImageField(upload_to='pictures')
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='General', 
                                 related_name = 'category')
    
    def __str__(self):
        return self.image.name
    
#model for the deleted pictures    
class DeletePicture(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='pictures')
    date_deleted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='General')
    
    def __str__(self):
        return self.image.name
    
   
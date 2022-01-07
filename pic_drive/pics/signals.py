from django.db.models.signals import pre_delete
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from . models import Picture, Category, DeletePicture, DeletedFolder
import datetime


@receiver(pre_delete, sender=Picture)
def log_deleted_pictures(sender, instance, using, **kwargs):
    d = DeletePicture()
    d.id = instance.id
    d.date_deleted = datetime.datetime.now() 
    d.category = instance.category
    d.image = instance.image
    d.owner = instance.owner
    d.save() 
    

@receiver(pre_delete, sender=Category)
def log_deleted_folders(sender, instance, using, **kwargs):
    d = DeletedFolder()
    d.id = instance.id
    d.date_deleted = datetime.datetime.now() 
    d.name = instance.name
    d.author = instance.author
    d.save()

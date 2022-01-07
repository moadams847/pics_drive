from django.contrib import admin
from .models import Picture, Category, DeletePicture, DeletedFolder

admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(DeletePicture)
admin.site.register(DeletedFolder)






from django.urls import path
from . import views 
from .views import (
                    CategoryListView, 
                    PictureListView, 
                    PictureDetailView, 
                    CategoryFolderCreateView,
                    CategoryFolderUpdateView,
                    CategoryFolderDeleteView
                    )

urlpatterns = [
  
   path('', CategoryListView.as_view(), name='pics-home'),
   path('picture_category/<str:name>/', PictureListView.as_view(), name='category-pics'),
   path('picture_category/<int:pk>/detail/', PictureDetailView.as_view(), name='detail-pics'),
   path('new/folder/', CategoryFolderCreateView.as_view(), name='new-folder'),
   path('new/folder/<str:name>/update/', CategoryFolderUpdateView.as_view(), name='update-folder'),
   path('new/folder/<str:name>/delete/', CategoryFolderDeleteView.as_view(), name='delete-folder'),




   
  
]

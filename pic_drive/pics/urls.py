from django.urls import path
from . import views 
from .views import (
                    CategoryListView, 
                    PictureListView, 
                    PictureDetailView, 
                    CategoryFolderCreateView,
                    CategoryFolderUpdateView,
                    CategoryFolderDeleteView,
                    PictureCreateView,
                    PictureUpdateView,
                    PictureDeleteView,
                    DeletedCategoryListView,
                    DeletedPictureListView,
                    DeletedPictureDetailView
                    )

urlpatterns = [
  
   path('', CategoryListView.as_view(), name='pics-home'),
   path('bin/', DeletedCategoryListView.as_view(), name='bin-pics'),

   path('folder/picture/<str:name>/', PictureListView.as_view(), name='category-pics'),
   path('bin/picture/<str:name>/', DeletedPictureListView.as_view(), name='bin-category'),

   
   path('folder/picture/<int:pk>/detail/', PictureDetailView.as_view(), name='detail-pics'),
   path('bin/picture/<int:pk>/detail/', DeletedPictureDetailView.as_view(), name='bin-detail'),

   
   path('folder/new', CategoryFolderCreateView.as_view(), name='new-folder'),
   path('folder/<str:name>/update/', CategoryFolderUpdateView.as_view(), name='update-folder'),
   path('folder/<str:name>/delete/', CategoryFolderDeleteView.as_view(), name='delete-folder'),
   path('folder/picture/<str:name>/new/picture/', PictureCreateView.as_view(), name='new-picture'),
   path('folder/picture/<int:pk>/update/', PictureUpdateView.as_view(), name='update-picture'),
   path('folder/picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='delete-picture'),








   
  
]

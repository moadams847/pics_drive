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
                    # CategoryPictureDeleteView,
                    ListDeletedPicturesView,
                    DeletedPictureDetailView,
                  DeletedPictureDeleteView,
                    )

urlpatterns = [
   path('', CategoryListView.as_view(), name='pics-home'),
   path('folder/picture/<str:name>/', PictureListView.as_view(), name='category-pics'),
   path('folder/picture/<int:pk>/detail/', PictureDetailView.as_view(), name='detail-pics'),
   path('folder/new', CategoryFolderCreateView.as_view(), name='new-folder'),
   path('folder/<str:name>/update/', CategoryFolderUpdateView.as_view(), name='update-folder'),
   path('folder/<str:name>/delete/', CategoryFolderDeleteView.as_view(), name='delete-folder'),
   path('folder/picture/<str:name>/new/', PictureCreateView.as_view(), name='new-picture'),
   path('folder/picture/<int:pk/update/', PictureUpdateView.as_view(), name='update-picture'),
   path('folder/picture/<int:pk>/delete/', views.PictureDeleteView, name='delete-picture'),
   path('bin/picture/', ListDeletedPicturesView.as_view(), name='recycled-picture'),
   path('bin/picture/<int:pk>/detail', DeletedPictureDetailView.as_view(), name='deletedPicture-detail'),
   path('bin/picture/<int:pk>/delete', DeletedPictureDeleteView.as_view(), name='deletedPicture-delete'),

#  path('folder/picture/<str:name>/new/picture/', PictureCreateView.as_view(), name='new-picture'),
#    path('folder/picture/<int:pk>/update/', PictureUpdateView.as_view(), name='update-picture'),

   
   
]

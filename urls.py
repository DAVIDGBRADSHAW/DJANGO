from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, AddPhotoView, ArticleRugbyView, AddPersonalDetails, EditPostView, EditPhotoView, UpdatePostView, DeletePostView, DeleteRugbyView,  AddCategoryView, AddCategoryRugbyView, CategoryView, ListView

urlpatterns =[
  path('', HomeView.as_view(), name="home"),
  
  path('article/<int:pk>', ArticleDetailView.as_view(), name="articles_detail"),
       
  path('AddPhotoView/<int:pk>', AddPhotoView.as_view(), name="photo_detail"),
  
  path('AddCatatoryRugbyView/<int:pk>', AddPhotoView.as_view(), name="photo_detail"),
  
  path('AddCategoryView/<int:pk>', AddPhotoView.as_view(), name="photo_detail"),
  
  path('AddPhotoView/<int:pk>', AddPhotoView.as_view(), name="photo_detail"),
  
  path('AddPhotoView/<int:pk>', AddPhotoView.as_view(), name="photo_detail"),
  
  path('EditPhoto/<int:pk>', EditPhotoView.as_view(), name="edit_photo_detail"),
  
  path('EditPostView/<int:pk>', EditPostView.as_view(), name="edit_detail"),

  path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_detail"),

  path('article/delete/<int:pk>/remove', DeletePostView.as_view(), name="delete_detail"),


  path('rugby/delete/<int:pk>', DeleteRugbyView.as_view(), name="delete_detail"),

  path('ArticleRugbyView/<int:pk>', ArticleRugbyView.as_view(), name="rugby_detail"),
  

  path('personal/<int:pk>', AddPersonalDetails.as_view(), name="personal_detail"),
  
  path('add_post/', AddPostView.as_view(), name='add_post'),

    
  path('add_category/', AddCategoryView.as_view(), name='add_category'),

  path('add_category_rugby/', AddCategoryRugbyView.as_view(), name='add_post'),

  path('category/<str:cats>/', CategoryView, name='category'),

  path('like/<int:pk>', LikeView, name='like_post'),
]
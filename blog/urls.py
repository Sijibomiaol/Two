from django.urls import path
from . import views 
from . views import PostListView, PostDetailView, PostCreateVeiw, PostUpdateVeiw, PostDeleteView, UserPostListView


urlpatterns=[
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 
    path('about/', views.about, name='about-us'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'),
    path('post/new/', PostCreateVeiw.as_view(), name= 'post-create'),
    path('post/<int:pk>/update/', PostUpdateVeiw.as_view(), name= 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
]
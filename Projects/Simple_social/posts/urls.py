from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path(r'by/(?P<username>[-\w+])', views.UserPosts.as_view(), name='for_user'),
    path(r'by/(?P<username>[-\w+])/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='single'),
    path(r'delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete')
]

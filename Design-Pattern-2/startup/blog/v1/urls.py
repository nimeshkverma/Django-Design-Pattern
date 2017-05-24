from django.conf.urls import url
import views


urlpatterns = [
    url('^about/$', views.AboutView.as_view(), name='about'),
    url('^$', views.PostListView.as_view(), name='post_list'),
    url('^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url('^post/new/', views.CreatePostView.as_view(), name='post_new'),
    url('^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name='post_update'),
    url('^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url('^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
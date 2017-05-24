from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/', include('blog.v1.urls'))
]
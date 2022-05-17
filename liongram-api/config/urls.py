from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.views import PostModelViewSet

#라우터는 uri를 쓸 수 있게 한다.
router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

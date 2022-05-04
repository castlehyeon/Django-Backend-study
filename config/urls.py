from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import index, url_view, url_parameter_view, function_view, class_view, function_list_view
#path에 변수<>를 넣을 수 있다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view), 
    path('url/<str:username>/', url_parameter_view) ,
    #str:username, int 불가능, 뒤에 숫자가 아니기 때문에
    #형태에 맞춰서 써야한다.
    #뷰에서 데이터를 받는 방법 3가지 
    #1. 경로변수지정 2. querystring (?key=value) 3. 폼을 이용하는 방법
    path('fbv/list', function_list_view),
    path('fbv/', function_view),
    #template->템플릿 파일이 없다고 에러메세지가 뜬다. s붙이기(폴더명이 다르면 안됨.)
    #settings.py에 template에 'APP_DIRS': True, 이는 템플릿을 쓰겠다는 의미
    path('cbv/', class_view.as_view(), name='cbv'),
    #함수는 그대로 넣지만, 클래스는 .as_view()를 붙인다. 
    #,를 찍어야함

    path('', index, name='index'),
    #path('accounts/', include('accounts.urls', namespace='accounts')),
    #include
    #path('__debug__/', include('debug_toolbar.urls')),
    path('posts/', include('posts.urls', namespace='posts')),

    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
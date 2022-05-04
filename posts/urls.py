from django.urls import URLPattern, path

from .views import post_list_view, post_create_view, post_detail_view, post_update_view, post_delete_view

app_name = 'posts'

urlpatterns = [
    #전체 목록 보여주기
    #''안의 경로내용이 바뀌더라도 name지정으로 자동으로 찾아가게 한다. 
    # template엔진은 이를 변수처럼 다룰 수 있게 해준다.
    # 동적으로 바꿀 수 있게 해준다. 
    path('', post_list_view, name='post-list'),


    #새로만들기
    path('new/', post_create_view, name='post-create'),
    #모델의 id를 상세히 보여주는 것.
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/edit/', post_update_view, name='post-update'),
    path('<int:id>/delete/', post_delete_view, name='post-delete'),

]
from django.contrib import admin
#Post 모델을 임포트, admin과 같은 경로 상에 있기 때문에 .models
from .models import Post, Comment

#admin.site.register(Post)
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    #(괄호 안에는 모델의 속성명을 넣어주는 것.)
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    #list_editable = ('content') -> 리스트 화면에서 수정이 바로 가능하다.
    
    #튜플형태 () 와 리스트형태 [] 는 다르다. 튜플형태일 때 마지막에 콤마를 넣어야한다.

admin.site.register(Comment)
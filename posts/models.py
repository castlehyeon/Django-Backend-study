from tkinter import CASCADE
from django.db import models
#django에서 제공하는 user테이블을 가져오기 위해
from django.contrib.auth import get_user_model

#유저 테이블 함수 호출
User = get_user_model()


#게시글
class Post(models.Model):
    #IM 이미지필드, verbose_name은 필드에 대한 이름 지정. 이미지필드는 경로 설정을 해줘야함.
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    #글 내용은 양이 많으므로 TextField,필수
    content = models.TextField(verbose_name='내용') 
    #게시 시간 로그, 필수, auto_속성값을 추가
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    #, 필수, default값은 0이다.
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    #게시글과 댓글은 모두 작성자가 들어감. //null은 실제로 DB에 null값을 허용하는가. blank도 유효성 검사에서 값이 없어도 허용할 것인가에 대해 명시.
    #작성자가 foreignkey로 묶여있는 것은 콤보박스로 들어간다.
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

#댓글
class Comment(models.Model):
    #댓글내용
    content = models.TextField(verbose_name='내용')
    #자동생성을 하게 되면 댓글을 올릴 때, 작성 시간을 임의로 수정할 수 없게 됨.
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    #게시글과 관계를 맺어줘야하기 때문에 ForeignKey, 게시글이 삭제되었을 때, 전부 삭제CASCADE
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    #사용자와 묶어주기 위해 ForeignKey, to = 다음에 '' 를 안쓰고 User를 바로 써준 이유는...?
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

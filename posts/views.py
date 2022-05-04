from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
#HttpResponse는 ()안에 html 코드를 읽을 수 있게 한다.
#content가 없으면 이를 html로 날리게 된다.
from django.views.generic.list import ListView
from .models import Post
#같은 패키지 내 models를 상속
from .forms import PostBaseForm

#templates 바로 아래 만들어줌.
def index(request):
    # post_list = Post.objects.all().select_related('writer').prefetch_related('comment_set').order_by('-created_at')
    #post_list = Post.objects.filter(writer=request.user)
    #Post.writer가 현재 로그인인 것 조회
    post_list = Post.objects.all().order_by('-created_at')
    #all() 공식문서 확인. Post 전체 데이터 조회
    #order_by는 최신순으로 '정렬'
    #all(), order_by 등의 쿼리셋API 내 함수 사용법 숙지.
    context = {
        'post_list': post_list
        #dictionary란 js의 객체와 유사. 
        #html파일에서 템플릿언어를 사용해서 딕셔너리를 쓸 수 있다. 
    }
    return render(request, 'index.html', context)
#settings 경로설정에서 templates까지 써줬기 때문에 ''에 posts폴더를 같이 써줘야함.  
#앱폴더내 별도의 urls파일을 만들어줌. 
def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)

#어노테이션, 로그인 체크
@login_required
def post_create_view(request):
    if request.method == 'GET':
        #데이터를 요청할 때
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')

        #DB에 생성
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user,
            #request.user란 user모델을 가져오는 것을 의미
        )

        return redirect('index')

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html', {'form': PostBaseForm()})
    else:
        form = PostBaseForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                content=form.cleaned_data.get('content'),
                writer=request.user,
            )
        else:
            return redirect('posts:post-create')

        return redirect('index')

def post_update_view(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'posts/post_form.html', context)
    else:
        new_image = request.FILES.get('image')
        content = request.POST.get('content')

        if new_image:
            post.image.delete()
            post.image = new_image

        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

def url_view(request):
    print('url_view()')
    data = {'code' : '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse(data)


def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    #f-string: 문자열 안에 변수 값을 삽입하는 용도
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    #if구문을 써서 출력할 때, GET과 POST 중 하나만 출력되도록 한다. (분기처리)
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    #일반적으로 데이터를 받을 때, 리소스를 받을 때 사용한다.
    #회원가입 폼을 받을 때.
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    #데이터를 추가, 수정, 삭제할 때 사용한다.
    #회원가입 요청 자체를 받을 때.
    return render(request, 'view.html')
    #함수기반 뷰
    
    #클래스기반 뷰(미리 만들어진 것을 가져다 쓰는 것.)
    #ListView를 ctrl+클릭 하면 코드를 뜯어볼 수 있다.
    #ListView를 사용하면 굉장히 편리하다.
class class_view(ListView):
    model = Post
    ordering = ['-id']
    #template_name = 'cbv_view.html'
    #만약 템플릿을 정의하지 않더라도, ListView에서 기본적인 약속이 있기 때문에.
    #모델만 상속받은 클래스뷰는 templates 폴더 내 
    #posts폴더의 post_list.html을 출력할 수 있다.
    #templates/APP이름/models이름  



    #이를 함수로 표현하면...(개발자가 직접 작성)
def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    #list.py의 쿼리셋 부분에서 all()을 그대로 가져와서 사용한다.
    return render(request, 'cbv_view.html', {'object_list' : object_list})

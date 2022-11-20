from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog,Photo
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainpage.html',{'blogs':blogs})



def detail(request,id):
    blog = get_object_or_404(Blog ,pk=id)
    return render(request, 'main/detail.html', {'blog':blog})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.body = request.POST['body']
    new_blog.save()
    for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.new_blog = new_blog
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
    return redirect('detail', new_blog.id)
            
def search(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.POST.get('q',"")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html',{'blogs' : blogs, 'q' : q})

    else:
        return render(request, 'search.html')


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Blog
from django.contrib import messages


def index(request):
    return render(request,'main/index.html')

@login_required
def create_blog(request):
    errors = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category =request.POST.get('category')
        description = request.POST.get('description')
        # image = request.FILES.get('image')

        # validation
        if not title:
            errors['title'] = "Title halnu parxa"
        
        if not category:
            errors['category'] = "Category select gara bhai"
        
        if not description:
            errors['description'] = "Description is required"
        
        # check it there is error or not
        if errors:
            return render(request,'main/create_blog.html',{'error':errors,'prev':request.POST})
        else:
            blog = Blog.objects.create(
                title=title,
                category= category,
                description = description,
                added_by = request.user
            )
            blog.save()
            messages.success(request,'Blog added successfully !! ')
            return redirect('index')

    return render(request,'main/create_blog.html')
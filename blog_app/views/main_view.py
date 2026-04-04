from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Blog
from django.contrib import messages


def index(request):
    try:
        blog = Blog.objects.all().order_by('-created_at')
    except Exception as e:
        print(e)
    return render(request,'main/index.html',{'blog1':blog})

@login_required
def create_blog(request):
    errors = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category =request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')

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
                image = image,
                description = description,
                added_by = request.user  
            )
            blog.save()
            messages.success(request,'Blog added successfully !! ')
            return redirect('index')

    return render(request,'main/create_blog.html')


# for getting the individual blog data
def single_method(request,id):
    # try:
    #     blog = Blog.objects.get(id=id)
    # except Exception as e:
    #     print(e)
    #     messages.error(request,"Blog does not exists")
    #     return redirect('index')
    blog = get_object_or_404(Blog,id=id)
    print(blog)
    return render(request,'main/single_page.html',{'blog':blog})


# for implement delete operation
def delete_blog(request,id):
    blog = Blog.objects.get(id=id)
    # check if the user is the owner of blog or not
    if blog.added_by == request.user:
        blog.delete()
        messages.success(request,"Blog deleted successfully")
        return redirect('index')
    else:
        messages.error(request,'You are not authorize to delete this blog !!')
        return redirect('single',id=id)
    
    



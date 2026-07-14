from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill, Blog
from .forms import ContactsForm, BlogsForm, CommentForm
from django.contrib import messages

# Create your views here.

# index view
def  index(request):
    return render(request,'index.html')

def skills(request):
    # retrieve  all records from the skills table
    skills = Skill.objects.all()
    return render(request,'skill.html',{'skills':skills})

def blog(request):
    # retrieve  all records from the blogs table
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})


def single_blog(request, id):
    blog=get_object_or_404(Blog,id=id)
    comments = blog.comments.all()
    form = CommentForm()
    context ={
        'blog':blog,
        'comments':comments,
        'form':form
    }
    return render(request,'details.html',context)

#view that handles new blog post
def create_blog(request):
    if request.method == 'POST':
        #create the object of the BlogsForm class
        form = BlogsForm(request.POST)
        if form.is_valid():
            #store the form content to the db
            form.save()
            messages.success(request,'New post Added successfully')
            return redirect('blog')
    else:
        form =BlogsForm()
    return render(request,'new.html',{'form':form})


def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
         #create the object of the BlogsForm class with an instance value
        form = BlogsForm(request.POST, instance=post)
        if form.is_valid():
            #store the edited form data to the db
            form.save()
            messages.success(request,f'Post updated successfully')
            return redirect('blog')
    else:
        form = BlogsForm(instance=post)
    return render(request, 'new.html',{'form':form, 'post':post})
        
        
def delete_post(request, id):
    # retrieve blog post with the  specified id else return 404 incase it doesnt exist
    post = get_object_or_404(Blog,id=id)
    
    #remove record from the db
    post.delete()
    messages.success(request,'Post Successfully deleted')
    #redirect back to blog page after delete
    return redirect('blog') 
          
def comment(request,id):
    blog = get_object_or_404(Blog,id=id)
    if request.method=="POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = blog
            comment.save()
            messages.success(request,'Comment added successful')
            return redirect('details',id=blog.id)
    

def contact(request):
    if request.method == 'POST':
        #instantiate the ContactsForm Class
        form = ContactsForm(request.POST)
        if form.is_valid():
            #save content of form to the db
            form.save()
            messages.success(request,'We have recieved your message(complaint). We will get back to you shortly')
    else:
        form =ContactsForm()
    return render(request, 'contact.html',{'form':form})
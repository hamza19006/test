from django.shortcuts import render,redirect, get_object_or_404
from .forms import MyForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = MyForm()
            return render(request, 'create.html', {'form':form})
    else:
        form = MyForm()
        return render(request, 'create.html', {'form':form})
    

def show_post(request , pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request, 'show_post.html', {'post':post})


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES, instance=post)
        if form.is_valid:
            form.save()
            return redirect('/' , pk= post.pk)
    else:
        form = MyForm()
        return render(request, 'update.html', {'form':form , 'post':post})
    


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')
        

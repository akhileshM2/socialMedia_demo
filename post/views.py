from django.shortcuts import render,redirect
from.models import Post
from.forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.
@login_required
def create_post(request):

    if request.method=="POST":
        form=PostForm(request.POST,files=request.FILES)
        if form.is_valid:
            post_item=form.save(commit=False)
            post_item.user=request.user
            post_item.save()
            msg=messages.success(request,"Post added!")
            return redirect('feed')
    else:
        form=PostForm()
        return render(request,'post/create.html',{'form':form})
    
@login_required
def feed(request):
    if request.method=="POST":
        comment_form=CommentForm(data=request.POST)
        new_comment=comment_form.save(commit=False)
        post_id=request.POST.get('post_id')
        post=get_object_or_404(Post,id=post_id)
        new_comment.post_field=post
        comment_id=request.POST.get('post_by')
        new_comment.posted_by=comment_id
        new_comment.save()
    else:
        comment_form=CommentForm()

    posts=Post.objects.all()
    return render(request,"post/feed.html",{"posts":posts,'comment_form':comment_form})

def like_post(request):
    post_id=request.POST.get('post_id')
    post=get_object_or_404(Post,id=post_id)

    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')





    
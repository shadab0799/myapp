from django.shortcuts import redirect,render,HttpResponse
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here
def bloghome(request):
    allPosts= Post.objects.filter(id=0)
    context={'allPosts': allPosts}
    return render(request, "blog/bloghome.html", context)



def dshome(request):
    allPosts= Post.objects.filter(id=1)
    context={'allPosts': allPosts}
    return render(request, "blog/dshome.html", context)
def jobhome(request):
    allPosts= Post.objects.filter(id=11)
    context={'allPosts': allPosts}
    return render(request, "blog/jobhome.html", context)
def lchome(request):
    allPosts= Post.objects.filter(id=2)
    context={'allPosts': allPosts}
    return render(request, "blog/lchome.html", context)
def aihome(request):
    allPosts= Post.objects.filter(id=3)
    context={'allPosts': allPosts}
    return render(request, "blog/aihome.html", context)


def blogpost(request, slug):
   if Post.objects.filter(slug=slug).first():
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogpost.html", context)
    #return redirect(f"/{post.slug}")
   else:
       return HttpResponse("<h1>page not found</h1>")


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/{post.slug}")
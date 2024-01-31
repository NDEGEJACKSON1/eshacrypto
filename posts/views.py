from django.shortcuts import render
from posts.models import Post
# from .models import Like, Comment
# from .forms import LikeForm, CommentForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts})


def post_details(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts' : posts})


# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     liked = False
#     if request.user.is_authenticated:
#         liked = Like.objects.filter(post=post, user=request.user).exists()
#     if request.method == 'POST':
#         if 'like' in request.POST:
#             like_form = LikeForm(request.POST)
#             if like_form.is_valid():
#                 like = like_form.save(commit=False)
#                 like.post = post
#                 like.user = request.user
#                 like.save()
#                 return redirect('post_detail', post_id=pk)
#         else:
#             comment_form = CommentForm(request.POST)
#             if comment_form.is_valid():
#                 comment = comment_form.save(commit=False)
#                 comment.post = post
#                 comment.user = request.user
#                 comment.save()
#                 return redirect('post_detail', post_id=pk)
#     else:
#         like_form = LikeForm()
#         comment_form = CommentForm()
#     comments = Comment.objects.filter(post=post)
#     return render(request, 'post_detail.html', {
#         'post': post,
#         'liked': liked,
#         'like_form': like_form,
#         'comment_form': comment_form,
#         'comments': comments
#     })


# def getPages(request,pk):

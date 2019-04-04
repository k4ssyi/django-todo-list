from django.shortcuts import render
from django.views.generic import View
from .models import Post


# Create your views here.
class PostIndex(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'post/post_list.html', context)

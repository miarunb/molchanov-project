from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import TagForm
from .models import Post, Tag
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={"posts": posts})

#def post_detail(request, slug):
    #post = Post.objects.get(slug__iexact=slug)
    #return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    #def get(self, request, slug):
        ##post = Post.objects.get(slug__iexact=slug)
        #post = get_object_or_404(Post, slug__iexact=slug)
        #return render(request, 'blog/post_detail.html', context={'post': post})


# def tag_detail(request, slug):
# tag = Tag.objects.get(slug__iexact=slug)
# return render(request, 'blog/tag_detail.html', context={'tag': tag})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})



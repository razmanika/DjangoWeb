from .models import User, Post, Comment
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class PostCreateView(generic.DetailView):
    model = Post # მოაქვს მოდელი და ამ მოდელის ობიექტები


class AllPostView(generic.ListView):
    template_name = 'blog/main.html'
    context_object_name = 'homeposts' # მოაქვს ყველა ობიექტი

    def get_queryset(self):
        return Post.objects.filter(publish_time__lte=timezone.now()).order_by('-publish_time')
    
    # def get_queryset(self):
    #     return Post.content(max_length = 20)


class PostDetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    # pk_url_kwarg = 'pk' # აქ მოდის pk_ს შესაბამისი პოსტი
    model = Post
    context_object_name = 'posts'

    
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw) # 
        post = self.get_object()
        context['comments'] = Comment.objects.filter(on_post=post)
        context['other_posts'] = Post.objects.filter(author=post.author).exclude(title=post.title)
        return context

# def comment_view(request, pk):
#     comm = get_object_or_404(Comment,pk=pk)
#     return render(request, 'blog/detail.html', {'comm':comm})




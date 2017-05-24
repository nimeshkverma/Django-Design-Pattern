from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm, CommentForm


class AboutView(TemplateView):
    template_name = 'blogs/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all().order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm


class UpdatePostView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')


@login_required
def add_comment_to_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', context={'form': form})

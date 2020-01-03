from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # or use object_list in the template if you don't set up a context name.
    context_object_name = 'posts'
    ordering = ['-date_posted']  # `-` indicates newest to oldest.


class PostDetailView(DetailView):
    model = Post


# LoginRequiredMixin is used in to class based views
# while @loginrequired decorator is for function based views.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Test if the current user is equal to the post's author.
    def test_func(self):
        # A method of the update view to get the post's attribute.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False # if False the response would be 403.


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # Test if the current user is equal to the post's author.
    def test_func(self):
        # A method of the update view to get the post's attribute.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html')

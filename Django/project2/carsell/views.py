from .models import Post
from .forms import CarSelectForm
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)


def home(request):
    form = CarSelectForm(request.POST)
    context = {
        'form': form,
        'title': 'Carsell',
        'posts': Post.objects.all(),
    }
    return render(request, 'carsell/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'carsell/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'make', 'model', 'image', 'year', 'color',
        'body_type', 'seats', 'doors', 'transmission_type',
        'configuration', 'engine_size', 'engine_type', 'mileage',
        'hp', 'price', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'make', 'model', 'image', 'year', 'color',
        'body_type', 'seats', 'doors', 'transmission_type',
        'configuration', 'engine_size', 'engine_type', 'mileage',
        'hp', 'price', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
        'title': 'Our Story',
    }
    return render(request, 'carsell/about.html', context)

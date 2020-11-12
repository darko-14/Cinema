from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from PIL import Image


class PostListView(ListView):
    paginate_by = 8
    model = Post
    template_name = 'app/movies.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 


class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post-detail.html'
    context_object_name = 'post'
    
    # def post(self, request, *args, **kwargs):
        
    
    #     title = request.POST.get('title')
    #     price = request.POST.get('price')
    #     date = request.POST.get('date')
        
        
    #     return render(request,'booking/booking.html', {
    #         'title': title, 
    #         'price':price, 
    #         'date':date,
    #     })


    
        

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'about', 'director', 'cast', 'premiere', 'content', 'price']
    template_name = 'app/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'about', 'director', 'cast', 'premiere', 'content', 'price']
    template_name = 'app/post_form.html'

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
    template_name = 'app/post_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'app/about.html')


def guide(request):
   return render(request, 'app/guide.html')




def movies(request):
    return render(request, 'app/home.html')




from django.shortcuts import redirect, render, get_object_or_404, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Picture, Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    ordering = ['-date_created']
    template_name = 'pics/home.html'    
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categories'] = context['categories'].filter(author=self.request.user)
        return context

class PictureListView(ListView):
    model = Picture
    context_object_name = 'pictures'
    ordering = ['-date_posted']
    template_name = 'pics/pictures_list.html'   
    
    def get_queryset(self):
        tag = get_object_or_404(Category, name=self.kwargs.get('name'))
        return Picture.objects.filter(category=tag).order_by('-date_posted') 
    
    def get_context_data(self, **kwargs):
        context = super(PictureListView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('name')
        return context
    
class PictureDetailView(DetailView):
    model = Picture
    context_object_name = 'picture'
    template_name = 'pics/picture_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetailView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('name')
        return context
class CategoryFolderCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'pics/new_folder.html'
    fields = ['name']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryFolderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'pics/new_folder.html'
    success_url = '/'

    # https://stackoverflow.com/a/62978825
    def get_object(self, queryset=None):
        return Category.objects.get(name=self.kwargs['name']) # instead of self.request.GET or self.request.POST

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False
    
class CategoryFolderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'pics/category_confirm_delete.html'
    success_url = '/'    

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False
    
    # https://stackoverflow.com/a/62978825
    def get_object(self, queryset=None):
        return Category.objects.get(name=self.kwargs['name']) # instead of self.request.GET or self.request.POST


class PictureCreateView(LoginRequiredMixin,CreateView):
    model = Picture
    template_name = 'pics/new_picture.html'
    fields = ['image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        name = self.kwargs.get('name')
        form.instance.category = Category.objects.get(name=name)
        return super().form_valid(form)
    
    # https://stackoverflow.com/a/62978825
    def get_object(self, queryset=None):
        return Category.objects.get(name=self.kwargs['name']) # instead of self.request.GET or self.request.POST

class PictureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Picture
   template_name = 'pics/new_picture.html'
   fields = ['image']
   success_url = '/'

   def form_valid(self, form):
       form.instance.owner = self.request.user
       name = self.kwargs.get('name')
       form.instance.category = Category.objects.get(name=name)
       return super().form_valid(form)
    
   def test_func(self):
        category = self.get_object()
        if self.request.user == category.owner:
            return True
        return False
    
class CategoryPictureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Picture
    template_name = 'pics/picture_confirm_delete.html'
    success_url = '/'    

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.owner:
            return True
        return False
    
   
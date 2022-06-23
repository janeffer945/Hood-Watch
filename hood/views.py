from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Business, Post, NeighborHood, Business
from .forms import NeighborHoodForm
from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'hood/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'hood/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


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
    return render(request, 'hood/about.html', {'title': 'About'})


def neighborhood(request):
    neighborhoods = NeighborHood.objects.all()
    context = {
        'neighborhoods':  neighborhoods,
        'title': 'Neighborhood' 
    }
    
    return render(request, 'hood/neighborhood.html', context)

def neighborhoodDetail(request,pk):
    neighborhood = NeighborHood.objects.get(id=pk)
    context = {
        'neighborhood':  neighborhood,
        'title': 'Neighborhood-detail' 
    }
    
    return render(request, 'hood/neighborhood_detail.html', context)

def biz(request):
    bizs = Business.objects.all()
    print(biz)
    context = {
        'bizs':  bizs,
        'title': 'Business' 
    }
    
    return render(request, 'hood/business.html', context)

def businessDetail(request,pk):
    biz = Business.objects.get(id=pk)
    context = {
        'biz':  biz,
        'title': 'Buisness-detail' 
    }
    
    return render(request, 'hood/buisness_detail.html', context)

def deleteNeighborhood(request, pk):
    try:
        hood = NeighborHood.objects.get(id=pk)
    except:
        messages.warning(request, 'neighbourhood Changed!!')
        
        
    if request.method == 'POST':
        hood.delete()
        messages.success(request, f'neighbourhood deleted!')
        return redirect('hood-home')
    return render(request, 'hood/delete.html', {'object':hood})


def updateNeighborhood(request, pk):
    hood = NeighborHood.objects.get(id=pk)
    form = NeighborHoodForm(instance=hood)
    
    if request.user != hood.user:
        return HttpResponse('Your are not allowed here!')
    if request.method == 'POST':
        form =  NeighborHoodForm(request.POST, instance=hood)
        if form.is_valid():
            form.save()
            messages.success(request,'hood updated succesfully')
            return redirect('hood-home')
    context = {
        'form': form
    }
    return render(request, 'hood/hood_form.html', context)



def createNeighborhood(request):
    form = NeighborHoodForm()
    if request.method == 'POST':
        form =  NeighborHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user= request.user
            hood.save()
            messages.success(request,'hood created succesfully')
            return redirect('neighborhood')
    context = {
        'form': form
    }
    return render(request, 'hood/hood_form.html', context)
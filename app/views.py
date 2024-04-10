from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm
from django.contrib import messages

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # ? Method to fetch context data for the template
        context = super().get_context_data(**kwargs)

        #? Fetch all Post objects from the database
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    #& View for rendering individual post detail pages
    template_name = 'detail.html'
    model = Post

class AddPostView(FormView):
    template_name='new_post.html'
    form_class=PostForm
    success_url='/'

    def dispatch(self,request,*args,**kwargs):
        self.request=request
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):

        new_object=Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request,messages.SUCCESS,'Your post was successfull')
        return super().form_valid(form)


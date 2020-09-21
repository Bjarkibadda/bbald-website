from django.shortcuts import render

# Create your views here.

from blog.models import Post

from django.views.generic import TemplateView, DetailView, ListView

class PostDetailView(DetailView):
    ''' view for each post '''
    model = Post
    template_name = 'post.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_list'] = Post.objects.all()
    #     return context

class PostsList(ListView):
    template_name = 'post_list.html'
    context_object_name = 'list_of_posts'
    queryset = Post.objects.filter(prj_or_blog=False)

class ProjectList(ListView):
    template_name = 'post_list.html'
    context_object_name = 'project_list'
    queryset = Post.objects.filter(prj_or_blog=True)

    
    
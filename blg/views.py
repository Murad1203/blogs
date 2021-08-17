from django.shortcuts import render, redirect
from .models import BlogApps, Category
# Create your views here.
from .forms import BlogsForm

from django.views.generic import ListView, DetailView, CreateView


class HomeBlog(ListView):
    model = BlogApps
    template_name = 'blg/blog.html'
    context_object_name = 'content'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return BlogApps.objects.filter(is_published=True)


class BlogByCategory(ListView):
    model = BlogApps
    template_name = 'blg/blog.html'
    context_object_name = 'content'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return BlogApps.objects.filter(category_id=self.kwargs['category_id'], is_published=True)



class ViewsBlogs(DetailView):
    model = BlogApps
    template_name = 'blg/get_blogs.html'




class CreateBlogs(CreateView):
    form_class = BlogsForm
    template_name = 'blg/add-news.html'





'''def add_news(request):

    if request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # return redirect(news)

    else:
        form = BlogsForm()
    return render(request, 'blg/add-news.html', {'form': form, })'''


'''
def get_category(request, category_id):
    content = BlogApps.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)

    return render(request, 'blg/category.html', {'content': content,
                                                 'category': category, })
'''
'''def get_blog(request, blog_id):
    item = BlogApps.objects.get(pk=blog_id)
    return render(request, 'blg/get_blogs.html', {'object': item})'''

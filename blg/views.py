from django.shortcuts import render, redirect
from .models import BlogApps, Category
# Create your views here.
from .forms import BlogsForm

def blog_views(request):

    content = BlogApps.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog.html', {'content': content,
                                         'categories': categories})



def get_category(request, category_id):
    content = BlogApps.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)

    return render(request, 'category.html', {'content': content,
                                             'categories': categories,
                                             'category': category, })


def add_news(request):
    global news
    if request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
        #return redirect(news)
    else:
        form = BlogsForm()
    return render(request, 'add-news.html', {'form': form, })

def get_blog(request, blog_id):

    item = BlogApps.objects.get(pk = blog_id)

    return render(request, 'get_blogs.html', {'item': item})
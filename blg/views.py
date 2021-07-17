from django.shortcuts import render

# Create your views here.

def blog_views(request):

    return render(request, 'blog.html')

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', blog_views, name = 'blog_views'),
    #path('category/<int:category_id>', get_category, name='category'),

    path('', HomeBlog.as_view(), name='blog_views'),
    path('add-news/', CreateBlogs.as_view(), name='add_news'),
    #path('add-news/',  add_news, name='add_news'),

    path('category/<int:category_id>', BlogByCategory.as_view(), name='category'),
    path('blog/<int:pk>', ViewsBlogs.as_view(), name='get_blog'),
    #path('blog/<int:blog_id>', get_blog, name='get_blog'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

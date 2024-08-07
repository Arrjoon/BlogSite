"""
URL configuration for Blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# from blog import views

from django.conf import settings
from django.conf.urls.static import static
from blog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('api/',include('blog.urls')),
    path('blog/<int:id>',views.blog_content,name='blog_content'),
    path('blog/form/',views.blog_form,name='blog_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
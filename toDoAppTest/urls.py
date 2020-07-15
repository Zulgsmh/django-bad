"""toDoAppTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),
    path('react/', TemplateView.as_view(template_name='tweets/react.html')),
    path('security/', include('security.urls')),
    path('craiglist/', include('craiglist_bad.urls')),
    path('todo/', include('todo.urls')),
    path('polls/', include('polls.urls')),
    
    path('tweets/', include('tweets.urls')),
    #path('api/tweets/', include('tweets.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL_TWEET_REACT, document_root=settings.STATIC_ROOT)

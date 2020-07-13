"""reddit_clone URL Configuration

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
from django.contrib import admin
from django.urls import path
from authentication.urls import urlpatterns as auth_urls
<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render
=======
from subreddit.urls import urlpatterns as subreddit_urls
from posts.urls import urlpatterns as posts_urls
>>>>>>> 16e3ecd03378c22bdd384e9d1b49173e710f2423
=======
from django.shortcuts import render
from subreddit.urls import urlpatterns as subreddit_urls
from posts.urls import urlpatterns as posts_urls

>>>>>>> 9546ac4edaee0a73113a5d6997607e02439b2028

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += auth_urls
<<<<<<< HEAD
<<<<<<< HEAD
=======
urlpatterns += subreddit_urls
urlpatterns += posts_urls
>>>>>>> 9546ac4edaee0a73113a5d6997607e02439b2028


def url_checker(request):
    for url in urlpatterns:
        if url not in urlpatterns:
            return render(request, '404.html')
<<<<<<< HEAD
=======
urlpatterns += subreddit_urls
urlpatterns += posts_urls
>>>>>>> 16e3ecd03378c22bdd384e9d1b49173e710f2423
=======
>>>>>>> 9546ac4edaee0a73113a5d6997607e02439b2028

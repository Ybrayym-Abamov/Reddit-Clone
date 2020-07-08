from django.urls import path

from authentication import views


urlpatterns = [
    #path('profile/<int:id>/', profile_view, name='profile'),
    path('', views.index, name='homepage'),
    path('login/', views.LoginView, name='login'),
    path('signup/', views.SignUpView, name='signup'),
]
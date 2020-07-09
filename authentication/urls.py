from django.urls import path
from authentication.views import LoginView, SignUpView, index, LogoutView


urlpatterns = [
    path('', index, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]

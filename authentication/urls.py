from django.urls import path
from authentication.views import LoginView, SignUpView, index, LogoutView, new, hot, following

urlpatterns = [
    path('', index, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new/', new, name='new'),
    path('hot/', hot, name='hot'),
    path('following/', following, name="following"),
]

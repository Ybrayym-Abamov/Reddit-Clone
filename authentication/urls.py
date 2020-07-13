from django.urls import path
from authentication.views import LoginView, SignUpView

urlpatterns = [
    # path('', views.index, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

from django.urls import path
from authentication.views import LoginView, SignUpView

urlpatterns = [
    # path('', views.index, name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]


handler404 = 'authentication.views.error_404_view'
handler403 = 'authentication.views.error_403_view'
handler400 = 'authentication.views.error_400_view'
handler500 = 'authentication.views.error_500_view'

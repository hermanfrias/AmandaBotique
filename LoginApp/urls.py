from django.urls import path
from LoginApp.views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='LoginApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='LoginApp/logout.html'), name='logout'),
    path('registrar/', registrar_usuario, name='registrar'),
    path('perfil/', perfil, name='perfil'),
    path('editar/', editar_perfil, name='editar_perfil'),
] 
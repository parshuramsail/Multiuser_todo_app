
from django.contrib import admin
from django.urls import path
from todo import views
from django.contrib.auth import views as authentication_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', authentication_view.LoginView.as_view(
        template_name='todo/login.html'), name='login'),
    path('logout/', authentication_view.LogoutView.as_view(
        template_name='todo/login.html'), name='logout'),

    path('signup/', views.signup),
    path('add-todo/', views.add_todo),
    path('delete-todo/<int:id>', views.delete_todo),
    path('change-status/<int:id>/<str:status>', views.change_todo),
]

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import myapp.views
import myaccounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', myapp.views.new, name='new'),
    path('create/',myapp.views.create,name='create'),
    path('',myapp.views.home,name='home'),
    path('blog/<int:blog_id>/',myapp.views.detail, name='detail'),
    path('edit/<int:blog_id>/',myapp.views.edit, name='edit'),
    path('destroy/<int:blog_id>/',myapp.views.destroy, name='destroy'),
    path('update/<int:blog_id>/',myapp.views.update, name='update'),
    path('singup/',myaccounts.views.signup, name='signup'),
    path('login/',myaccounts.views.login, name='login'),
    path('logout/',myaccounts.views.logout,name='logout'),
    path('newblog/',myapp.views.blogpost,name="newblog"),
]

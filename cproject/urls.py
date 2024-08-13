"""
URL configuration for cproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from capp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('con',views.ContactView.as_view(),name="con_view"),
    path('view',views.ListContact.as_view(),name="view"),
    path('del<int:id>',views.TodoDeleteView.as_view(),name="del_view"),
    path('upd<int:id>',views.TodoUpdateView.as_view(),name="upd_view"),

]

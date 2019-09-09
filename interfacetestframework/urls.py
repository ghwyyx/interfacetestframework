"""interfacetestframework URL Configuration

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
from django.views.generic.base import RedirectView
from django.urls import path
from interfacetestapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="interface")),
    path('interface/', views.simple_interface, name='interface_id'),
    path('interface/a.html', views.simple_interface, name='interface_id'),
    path('interface/b.html', views.showinterfacelist, name='interface_list'),
    path('interface/c.html', views.showinterfaceresult, name='interface_result'),
    path('showinterfacelist/', views.getinterfacelistdata, name='interface_data_list'),
    path('dealallrequests/', views.dealallrequests, name='interface_deal_requests'),
    path('interface/d.html', views.showallrequests, name='interface_show_deal_requests'),
]

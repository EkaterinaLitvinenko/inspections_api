"""inspection_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from datastore.views import StkView, EkView, PzpView, ZnamkaView, KmView

urlpatterns = [
    path('stk/<str:vin>/', StkView.as_view(), name='stk-detail'),
    path('ek/<str:vin>/', EkView.as_view(), name='ek-detail'),
    path('pzp/<str:vin>/', PzpView.as_view(), name='pzp-detail'),
    path('znamka/<str:vin>/', ZnamkaView.as_view(), name='znamka-detail'),
    path('km/<str:vin>/', KmView.as_view(), name='km-detail'),
]

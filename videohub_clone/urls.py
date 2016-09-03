"""videohub_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

def redirect_to_hub(request):
    return redirect('hub:index')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hub/', include('hub.urls', namespace='hub')),

    # Root 로 접속하면, 지정 뷰로 이동
    # 1) lambda 함수로 뷰 지정
    # url(r'^$', lambda request: redirect('hub:index')),
    # 2) 함수로 뷰 지정
    # url(r'^$', redirect_to_hub),
    # 3) 클래스 기반 뷰 (Class Based View) 로 지정
    url(r'^$', RedirectView.as_view(pattern_name='hub:index')),
]

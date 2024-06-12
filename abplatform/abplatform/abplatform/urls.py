"""
URL configuration for abplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from ab_app.views import IndexView,HypothesesView,MetricsView,BoardView,AddMetricsView,DesignABView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',IndexView.as_view(),name='home'),
    path('metrics',MetricsView.as_view(),name='metrics'),
    path('hypotheses',HypothesesView.as_view(),name='hypotheses'),
    path('tests', MetricsView.as_view(), name='tests'),

    path('tests/design', DesignABView.as_view(), name='design'),
    path('tests/report', HypothesesView.as_view(), name='report'),
    path('tests/board', BoardView.as_view(), name='board'),

    path('metrics/add', AddMetricsView.as_view(), name='add_metrics')

]

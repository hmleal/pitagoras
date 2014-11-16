from django.conf.urls import patterns, url
from core import views


urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^analises/$', views.AnalyzesView.as_view(), name='analyzes'),
    url(r'^analises/grafo/$', views.GrafoView.as_view(), name='grafo'),
    url(r'^analises/results/$', views.result, name='results')
)

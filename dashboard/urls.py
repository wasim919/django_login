from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.dashboard_index, name = 'dashboard_index'),
    url(r'^details/(?P<pk>\d+)/$', views.announcement_detail, name = 'announcement_detail'),
    url(r'^profile/', views.profile, name = 'profile'),
]

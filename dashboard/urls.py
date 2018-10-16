from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url('^$', views.dashboard_index, name = 'dashboard_index')
]
